import cv2
import mediapipe as mp
import time

# Capture video from the default camera (webcam)
cap = cv2.VideoCapture(0)

# Initialize Mediapipe Hand module
mpHands = mp.solutions.hands
hands = mpHands.Hands()  # Create an instance of the Hands module
mpDraw = mp.solutions.drawing_utils  # Utility for drawing hand landmarks

# Initialize variables for calculating FPS
pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert the frame to RGB (Mediapipe works with RGB)
    results = hands.process(imgRGB)  # Process the image to detect hands
    # print(results.multi_hand_landmarks)  # Uncomment to print hand landmarks data

    if results.multi_hand_landmarks:  # Check if any hand landmarks are detected
        for handLms in results.multi_hand_landmarks:  # Iterate through detected hands
            for id, lm in enumerate(handLms.landmark):  # Iterate through all landmarks of the hand
                # print(id, lm)  # Uncomment to print landmark ID and position

                # Get the dimensions of the image
                h, w, c = img.shape
                # Convert landmark coordinates from relative to absolute values
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)  # Print landmark ID and its pixel position

                if id == 8:  # Check if the landmark ID is 8 (Index fingertip)
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)  # Draw a circle on the fingertip

            # Draw hand landmarks and connections on the image
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            # Calculate Frames Per Second (FPS)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Display FPS on the screen
    cv2.putText(img, str(int(fps)), (10, 78), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 255), 3)

    # Show the output image with hand tracking
    cv2.imshow("Image", img)
    cv2.waitKey(1)  # Wait for a key press (1ms delay for real-time processing)
