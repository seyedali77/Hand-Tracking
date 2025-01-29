# Hand-Tracking
Hand Tracking with OpenCV & Mediapipe
This project implements real-time hand tracking using OpenCV and Mediapipe. It detects hands from a webcam feed, tracks hand landmarks, and displays their positions. Additionally, it calculates and displays the FPS (Frames Per Second) for performance monitoring.

Features
 Detects multiple hands in real-time
 Draws hand landmarks and connections
 Tracks specific landmark positions (e.g., index fingertip)
 Displays FPS for performance analysis

Installation
Before running the script, ensure you have Python and the required libraries installed. You can install dependencies using:


pip install opencv-python mediapipe
Usage
Run the script to start real-time hand tracking:


python hand_tracking.py
Controls
The script captures webcam input and detects hands.
It tracks hand landmarks and highlights the index fingertip (landmark ID 8).
FPS is displayed on the screen to monitor real-time performance.
Press Esc or close the window to exit.

Code Explanation
handDetector Class

Uses Mediapipe’s Hands module for hand detection and tracking.
findHand(img): Detects hands and draws landmarks.
findPosition(img, handNo=0): Returns landmark positions.
main() Function

Captures frames from the webcam.
Uses handDetector to track hands.
Prints index fingertip coordinates (lmList[8]).
Displays FPS on the screen.
Example Output
The script will display a real-time webcam feed with hand landmarks and FPS:

(Replace with an actual image of your output)

Future Improvements
 Add gesture recognition (e.g., counting fingers, detecting specific gestures)
 Improve landmark tracking accuracy
 Implement hand gesture-based controls for applications

Credits
🔹 Developed using OpenCV and Mediapipe
🔹 Inspired by Machine Learning & Computer Vision techniques
