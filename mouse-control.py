import cv2
import mediapipe as mp
import pyautogui
import urllib.request
import os
import math
import time

MODEL_PATH = "hand_landmarker.task"

MODEL_URL = (
    "https://storage.googleapis.com/"
    "mediapipe-models/hand_landmarker/"
    "hand_landmarker/float16/1/hand_landmarker.task"
)

SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
SMOOTHING = 0.25
CLICK_DISTANCE = 35
CLICK_COOLDOWN = 0.5

if not os.path.exists(MODEL_PATH):
    print("Downloading MediaPipe hand model...")
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
    print("Model downloaded successfully!")

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
RunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=MODEL_PATH),
    running_mode=RunningMode.VIDEO,
    num_hands=1,
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5,
    min_tracking_confidence=0.5
)

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("ERROR: Could not open webcam.")
    exit()

previous_x = 0
previous_y = 0
last_click_time = 0
frame_timestamp = 0

def distance(point1, point2, width, height):
    x1 = int(point1.x * width)
    y1 = int(point1.y * height)
    x2 = int(point2.x * width)
    y2 = int(point2.y * height)

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def finger_is_up(hand_landmarks, tip_id, pip_id):
    return hand_landmarks[tip_id].y < hand_landmarks[pip_id].y

with HandLandmarker.create_from_options(options) as landmarker:

    while True:
        success, frame = camera.read()

        if not success:
            break

        frame = cv2.flip(frame, 1)
        height, width, _ = frame.shape

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        frame_timestamp += 33

        result = landmarker.detect_for_video(
            mp_image,
            frame_timestamp
        )

        if result.hand_landmarks:
            hand_landmarks = result.hand_landmarks[0]

            thumb_tip = hand_landmarks[4]
            index_tip = hand_landmarks[8]
            middle_tip = hand_landmarks[12]

            index_up = finger_is_up(
                hand_landmarks, 8, 6
            )

            middle_up = finger_is_up(
                hand_landmarks, 12, 10
            )

            ring_up = finger_is_up(
                hand_landmarks, 16, 14
            )

            pinky_up = finger_is_up(
                hand_landmarks, 20, 18
            )

            for landmark in hand_landmarks:
                x = int(landmark.x * width)
                y = int(landmark.y * height)

                cv2.circle(
                    frame,
                    (x, y),
                    5,
                    (0, 255, 0),
                    -1
                )

            index_x = int(index_tip.x * width)
            index_y = int(index_tip.y * height)

            cv2.circle(
                frame,
                (index_x, index_y),
                12,
                (255, 0, 0),
                2
            )

            if (
                index_up
                and not middle_up
                and not ring_up
                and not pinky_up
            ):
                target_x = index_tip.x * SCREEN_WIDTH
                target_y = index_tip.y * SCREEN_HEIGHT

                current_x = previous_x + (
                    target_x - previous_x
                ) * SMOOTHING

                current_y = previous_y + (
                    target_y - previous_y
                ) * SMOOTHING

                pyautogui.moveTo(
                    current_x,
                    current_y
                )

                previous_x = current_x
                previous_y = current_y

                cv2.putText(
                    frame,
                    "MOVE",
                    (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

            click_distance = distance(
                thumb_tip,
                index_tip,
                width,
                height
            )

            if click_distance < CLICK_DISTANCE:
                current_time = time.time()

                if current_time - last_click_time > CLICK_COOLDOWN:
                    pyautogui.click()
                    last_click_time = current_time

                    cv2.putText(
                        frame,
                        "CLICK",
                        (20, 90),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 255),
                        2
                    )

            if (
                index_up
                and middle_up
                and not ring_up
                and not pinky_up
            ):
                if index_tip.y < 0.4:
                    pyautogui.scroll(2)
                elif index_tip.y > 0.6:
                    pyautogui.scroll(-2)

                cv2.putText(
                    frame,
                    "SCROLL",
                    (20, 130),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 0),
                    2
                )

            if (
                not index_up
                and not middle_up
                and not ring_up
                and not pinky_up
            ):
                cv2.putText(
                    frame,
                    "STOP",
                    (20, 170),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2
                )

        cv2.imshow(
            "Hand Gesture Mouse Control",
            frame
        )

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

camera.release()
cv2.destroyAllWindows()