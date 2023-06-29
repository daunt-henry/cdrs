# Cricket Decision Review System (CDRS)

The Cricket Decision Review System (CDRS) is a Python-based software application that enables users to review and analyze critical moments in cricket matches. This decision-making tool utilizes the powerful combination of the tkinter and cv2 libraries to provide a comprehensive solution for accurate decision-making during cricket games.

## Key Features

- **Video Playback and Navigation:** CDRS allows users to upload cricket match footage and provides controls for video playback, including frame-by-frame analysis. Users can navigate through the video to review specific moments in detail.

- **Ball Tracking and Speed Calculation:** Using advanced computer vision algorithms, CDRS accurately tracks the trajectory of the cricket ball in real-time. The software also calculates the speed of the delivered ball based on its frame-to-frame movement, providing valuable insights into bowler performance.

- **Decision Review System (DRS) Integration:** CDRS includes a user-friendly DRS module that enables users to challenge on-field umpire decisions. By selecting specific moments in the video and utilizing available resources, users can simulate DRS scenarios and determine whether a decision should be overturned or upheld.

- **Visual Feedback and Pending Decisions:** During the review process, CDRS provides visual feedback to indicate pending decisions. It displays relevant images and text, such as "DECISION PENDING," enhancing the overall user experience and replicating the real-world decision review process.

- **Out and Not Out Decisions:** CDRS allows users to make the final decision by selecting either the "Give out" or "Give Not Out" buttons. The software displays appropriate images, such as "OUT.jpg" or "NOT OUT.jpg," to represent the decision made.

## Getting Started

1. Clone the repository to your local machine or download the source code.
2. Ensure you have Python installed on your system.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Replace the sample video file (`video1.mp4`) with your own cricket match footage in the appropriate format.
5. Customize the images used for visual feedback, such as "pending.jpg," "SPONSER.jpg," "OUT.jpg," and "NOT OUT.jpg," to fit your preferences.
6. Run the application using the command `python main.py`.

## Usage

- Upon launching the application, the main window will display a cricket-related welcome image.
- Use the provided buttons to control video playback, allowing you to move forward or backward at different speeds.
- When a critical moment requires a decision, press either the "Give out" or "Give Not Out" button to simulate the decision.
- The software will display appropriate images representing pending decisions, sponser ads, and the final out or not out decision.
- Enjoy analyzing and reviewing cricket match moments with CDRS!

## Contributing

Contributions to the Cricket Decision Review System (CDRS) are welcome! If you have any ideas, suggestions, or bug reports, please submit them via the issue tracker. Feel free to fork the repository and submit pull requests for enhancements or bug fixes.

## License

The Cricket Decision Review System (CDRS) is open-source software licensed under the [MIT License](https://opensource.org/licenses/MIT). Please review the `LICENSE` file for more details.

## Acknowledgements

We would like to acknowledge the following resources and libraries that made the development of CDRS possible:

- [OpenCV](https://opencv.org/): An open-source computer vision library used for video processing and analysis.
- [tkinter](https://docs.python.org/3/library/tkinter.html): The standard Python interface for creating graphical user interfaces.
- [imutils](https://github.com/jrosebr1/imutils): A set of convenience functions to make basic image

 processing functions such as resizing and rotation easier with OpenCV.
- [Pillow](https://python-pillow.org/): A friendly fork of the Python Imaging Library (PIL) used for image processing and manipulation.

## Contact

For any questions, feedback, or inquiries, please contact [daunthenry462@gmail.com](mailto:your-daunthenry462@gmail.com).

Happy reviewing and analyzing cricket match moments with CDRS!
