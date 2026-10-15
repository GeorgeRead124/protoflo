# -*- coding: utf-8 -*-
"""All site content lives here. Photo ids: p<N> = 'unnamed (N).png', j<N> = 'unnamed (N).jpg',
p0 = 'unnamed.png', j0 = 'unnamed.jpg'. Edit text/links/photos here, then run: python build.py"""

NAME = "George Read"
FULL = "George Yaccoup Altaweel Read"
TAGLINE = "Mechatronics and Robotics Engineering · Assiut University"
PHONE = "+201030167198"
ADDRESS = "Egypt, Assiut"
EMAILS = ["georgeyaccoup124@gmail.com", "georgeread124@gmail.com", "jorje.eltaweel@eng.aun.edu.eg"]
RESUME = "https://drive.google.com/file/d/1xLezP3o81pXRpRXxeOxk9F3aaRt-gBpb/view?usp=sharing"
RESUME_PREVIEW = "https://drive.google.com/file/d/1xLezP3o81pXRpRXxeOxk9F3aaRt-gBpb/preview"
FORM = "https://docs.google.com/forms/d/e/1FAIpQLSd8nn_WpLrHY5jV5SJzPiBdSsbkWQz-CBs0Tmbnlb9qqT5AoQ/viewform?usp=sharing"
OLD_SITE = "https://sites.google.com/view/georgeread/"
SOCIAL = [
    ("LinkedIn", "https://www.linkedin.com/in/george-yaccoup/"),
    ("GitHub", "https://github.com/georgeyaccoup"),
    ("Google Scholar", "https://scholar.google.com/citations?user=r1-InQ8AAAAJ&hl=en"),
    ("X", "https://x.com/yaccoupgeorge"),
    ("Instagram", "https://www.instagram.com/george_yaccoup124/"),
    ("Facebook", "https://www.facebook.com/share/1CzhpdvQAa/"),
]
VIDEO_BIO = "Rc7--QmobW4"
VIDEO_RESEARCH = "3ToAt5vHuDQ"

# slug, nav label, title, intro
PAGES = [
    ("index", "Bio", "Bio", ""),
    ("research", "Research", "Research Experience", ""),
    ("projects", "Projects", "Projects", "Since the beginning of my university journey, I decided to approach every project as an opportunity for development and innovation. Facing rejection from my university and community when seeking undergraduate research opportunities, I transformed these obstacles into motivation by using each challenge as preparation for a future career in research and development (R&D)."),
    ("experience", "Experience", "Internships and Working Experience", "My professional experience began at a very young age. At 15, I learned how to code in C, and by 16, I secured my first project through LinkedIn. After that, I focused on developing my skills further to prepare myself for internships and real-world projects."),
    ("skills", "Skills", "Tech and Non-Tech Skills", ""),
    ("community", "Community", "Student Activities and Community Service", "I don’t just want to build robots, I want to build a place where knowledge is shared, talent grows without privilege, and every person has the chance I once fought for. That’s the future I’m building."),
    ("presentations", "Presentations", "Presentations", "Mastering presentation skills has been one of my key priorities for the last five years, during which I’ve delivered over 50 presentations ranging from academic talks to pitch decks and project demonstrations."),
    ("courses", "Courses", "Courses", "Courses inside class and extra courses outside class."),
    ("certificates", "Certificates", "Certificates", "Certificates, awards and letters of recognition."),
]

HERO = "p0"

BIO_STORY = [
    "I grew up in a small rural town in Egypt, where resources were scarce but curiosity was endless. At 15, I taught myself C programming and electronics, turning my free time into a world of discovery. By 16, I had completed my first embedded systems project, proving to myself (and others) that innovation can begin anywhere.",
    "My journey is built on resilience, self-learning, and service. From teaching hundreds of people computer and robotics skills through Tech Spot, a free academy I founded, to representing my university in robotics competitions, I’ve learned that technology is not just about machines, but about empowering people.",
]
BIO_ALONG = [
    "Mastered ROS2, embedded systems, and robotics simulation.",
    "Got a full scholarship from USAID scholars.",
    "Published research on energy optimization in robotics.",
    "Interned with Siemens, ExxonMobil, Halliburton, Fab Lab Egypt, and more, applying innovation to real-world engineering challenges.",
    "Studied abroad at Temple University (USA), where I joined robotics labs, collaborated with PhDs, and even built a mini pupper robot that danced.",
]
BIO_VISION = "To reduce robotics’ power consumption, building adaptation control systems, and smart mechanical design, all controlled by smart multi-layered ML techniques; build Egypt’s first Robotics R&D hub; and prove that innovation isn’t a privilege, it’s the reward of perseverance."
BIO_OUTRO = [
    "When I’m not building robots, you’ll find me mentoring, competing in robotics challenges, or exploring football fields and new cultures.",
    "I’d love to connect with researchers, engineers, and dreamers who share the belief that technology can reshape lives and communities.",
]
BIO_ENJOY = ["Playing and watching soccer.", "Playing Ping-Pong and Chess."]
FEEDBACK = "I would appreciate it if you left me some feedback about my work, advice for my development, or any comments. (you can just scan the QR code)"

STATS = [("7", "industry internships"), ("125+", "students taught directly"), ("50+", "presentations delivered"), ("38.7%", "max. simulated energy saving")]

# ---------------------------------------------------------------- RESEARCH
RESEARCH_INTERESTS = [
    "Soft Robotics integration and Bio-Inspired Robotics.",
    "Mobile Robotics Navigation using Machine Learning.",
    "Marine Robotics Navigation using Machine Learning.",
    "Robotics Energy consumption using Deep Learning.",
    "Medical Robots and Robots training.",
    "Increasing safety and generalization of Robotics control systems using ML.",
]
RESEARCH = [
    dict(slug="energy-paper", badge="Published paper", date="March to Sept 2025",
         title="Optimizing Energy Consumption in Robotics Using Linear Regression for Control Parameter Prediction",
         link=("Read on IEEE Xplore", "https://ieeexplore.ieee.org/abstract/document/11384715"),
         paras=["Robotic systems are increasingly used across industries, but their high energy consumption raises economic and environmental concerns. To address this, we developed a linear regression-based predictive control approach that optimizes energy use by forecasting suitable control parameters. Using ROS2-Gazebo, we simulated around 1,700 pick-and-place operations on a 6-DOF KUKA KR16 L6 robot under varying payloads, trajectories, and control settings. The model successfully predicted energy-optimal parameters, reducing simulated energy consumption by 17.8%–38.7% compared to baseline controls, while maintaining task performance. These results demonstrate that even simple machine learning models like linear regression can achieve significant energy savings in robotics when integrated into real-time control environments."],
         file=("903139_Conferance Presentation.pptx", "files/presentations/903139_Conferance Presentation.pptx"),
         video=VIDEO_RESEARCH, imgs=["p4"]),
    dict(slug="desalination", badge="Entrepreneurship · AUC & USAID", date="Semester: Feb 24 – July 24",
         title="Desalination of water using Freezing Desalination (Desalination Machine)",
         paras=["We designed and built a freezing desalination machine capable of producing 5 liters of clean water per hour from saline sources. By applying optimized thermodynamic processes and control strategies, the system achieved an 18% reduction in energy consumption compared to conventional methods. Throughout the project, I developed strong skills in thermodynamics, mechanical design, and STM32 programming, integrating hardware and software to create an efficient, sustainable water purification solution.",
                "As part of my work with the Entrepreneur with CEI program supported by AUC and USAID, my team and I at Frozen Mind developed and experimentally investigated a novel spray freezing desalination system for sustainable seawater purification. The project aimed to optimize freshwater recovery using an indirect contact falling film freezing method, where saline water is sprayed as droplets onto cooled surfaces to form pure ice crystals while rejecting salt and impurities. The system utilizes a simple refrigeration cycle with R-134a refrigerant and ethanol as a cooling medium, enhancing heat transfer efficiency and reducing energy consumption. Our design achieved a 12% increase in water recovery efficiency compared to conventional systems and demonstrated significant potential to exceed 80% efficiency with optimized parameters. This innovative approach minimizes energy use, eliminates the need for post-washing, and offers an environmentally friendly solution to global water scarcity challenges."],
         imgs=["j0", "p2"]),
    dict(slug="pear-sorting", badge="Currently · graduation project research", date="Sept 2025",
         title="Solar-Powered Intelligent Sorting and Packaging Machine for Agricultural Products",
         paras=["This research aims to design and implement a solar-powered intelligent sorting and packaging machine for pears. The system combines mechanical, vision-based, and robotic technologies to automate the full process of fruit handling.",
                "The sorting process begins with a mechanical mechanism that separates pears based on size. A computer vision system, enhanced by a machine learning model with reinforcement learning, identifies the quality of pears by detecting defects and infections. Based on this classification, the machine directs fruits into appropriate packaging paths.",
                "The packaging stage is managed by two robotic arms: one arranges large, high-quality pears into a premium layer at the top of the package, while the other organizes smaller good pears in the lower layers. This dual strategy ensures better product presentation and market value.",
                "The system is powered by a solar energy unit, enabling operation in outdoor farm environments with reduced reliance on external power. In addition, the project integrates automation, PLCs, IoT connectivity, and ROS-based control to achieve a robust, scalable, and efficient solution.",
                "By combining automation, robotics, AI, and renewable energy, this project provides a sustainable and cost-effective approach to improving agricultural efficiency, reducing waste, and supporting Egypt’s transition to smart farming technologies."],
         imgs=["p9"]),
]
RESEARCH_CURRENT = ["Alongside Dr. Abdallah Farage, Dr Gmal Abdelnasser, and Dr. Ahmed Saed, we are working on expanding the last published paper, applying more advanced machine learning approaches with advanced control systems.",
                    "Autonomous Vision-Based Robotic System for Pear Inspection, Infection Detection, and Smart Packaging"]
PEAR_ABSTRACT = "This research presents the design and implementation of an intelligent, autonomous sorting and packaging system for agricultural products, specifically focused on pears. Utilizing a multi-stage vision pipeline and a Jetson Nano edge-computing platform, the system integrates classical computer vision, deep learning, and geometric modeling to facilitate real-time quality control and mass prediction. The system architecture encompasses fruit localization, pathological inspection, and mass estimation via depth-to-volume mapping to drive a closed-loop robotic manipulation and conveyor control sequence."
PEAR_METHOD = [
    ("Multi-Space Object Detection and Localization", "Initial fruit detection is achieved through a multi-layered classical computer vision approach. By analyzing color distributions across three distinct color spaces (HSV, LAB, and BGR), the system generates comprehensive histograms for comparison against a baseline distribution. This tiered verification ensures high-fidelity pear identification. Non-conforming objects trigger an immediate rejection protocol via a 6-axis servo-actuated gripper."),
    ("Automated Pathological Inspection", "Post-localization, the pears undergo a secondary inspection phase using a pre-trained TensorFlow convolutional neural network (CNN). The model is optimized for infection detection and classification. Any fruit identified with pathological defects is systematically rejected, while healthy specimens proceed to the metric analysis stage."),
    ("Volumetric Analysis and Mass Prediction", "Using an Intel RealSense D455 depth camera, the system captures a dense point cloud (exceeding 1,000 data points) to reconstruct the surface geometry of the fruit. By generating curves that define the surface plane, the system estimates the volume of the pear. These geometric parameters are then processed through an Online-Trained Linear Regression (LR) model to predict fruit mass. This mass value serves as a critical input for the closed-loop control of the robotic packaging arm, ensuring precise force and motion planning."),
    ("Vision-Based Motion Control and System Synchronization", "The vision system further functions as the primary sensor for temporal tracking. By monitoring the entry and exit timestamps of fruit within the field of view, the system calculates the real-time velocity of the conveyor. This data facilitates a closed-loop feedback mechanism, synchronizing the conveyor speed with the processing latency of the vision pipeline and the robotic manipulation cycles."),
]
PEAR_RESULTS = [
    ("96%", "Object detection", "The multi-space histogram analysis achieved a 96% detection accuracy."),
    ("86%", "Mass prediction", "The online-trained Linear Regression model reached an accuracy of 86%, with performance expected to improve as the dataset expands."),
    ("0", "Critical failures", "Testing indicates a smooth operational flow with zero critical system failures during integrated sorting and packaging cycles."),
]
PEAR_IMGS = ["p7", "p8", "p5"]

# ---------------------------------------------------------------- PROJECTS
CATS = {"robotics": "Robotics", "embedded": "Embedded & Software", "automation": "Automation & PLC",
        "modelling": "Modelling & Control", "mechanical": "Mechanical Design"}

GH = "https://github.com/georgeyaccoup/"
LI = "https://www.linkedin.com/posts/"
DR = "https://drive.google.com/drive/folders/"

GRAD = dict(
    title="Graduation Project: Solar-Powered Intelligent Fruit Sorting and Packing System Based on Industry 4.0 Technologies",
    imgs=["p60", "p5"],
    blocks=[
        dict(h="Vision – AI system", imgs=["p6"], bullets=[
            "Designing the vision control flow using Jetson Nano with depth camera, working on control system using PID and MPC. Achieving 98% accuracy alongside estimating the Mass, Volume, Surface area, and size.",
            "Also the vision system operates as the main controller for 4 feedback loops, controlling 2 conveyors, 6 servo motors (delay time), Robotic Arm."]),
        dict(h="Robotic Arm", imgs=["p11", "p10"], caps={"p11": "Assembled gripper module: manifold housing, standoffs, extension mast, and cup-holder plate (with pneumatic tubing) suspended from the gantry beam.", "p10": "Close-up of the extension mast head: the 3D-printed enclosure houses the lift motor and its coupling to the vertical column."}),
        dict(h="Fabrication", imgs=["p55", "p56", "p57"], text="Fabricating and manufacturing 3D printed components and all fabricated tools used on the machine, including:",
             bullets=["Gripper.", "Robotic Arm.", "Vision systems.", "Spacers.", "Motors Holders.", "Sensors Holders.", "Camera Box and Holders."]),
        dict(h="Pneumatic Circuit", imgs=["p58", "p39"], bullets=[
            "Pneumatic vacuum circuit: compressor → filter-regulator → 3/2 solenoid valve → Venturi ejector → dual 1 in/12-out manifolds → twelve suction cups.",
            "De-energized (fail-safe) state: The valve is 3/2 normally closed, so with no electrical signal the supply path is blocked, and the vacuum line is vented to atmosphere. The gripper cannot hold a load with power or signal lost and cannot accidentally energize on a control fault."],
             file=("SAAT_Book.pdf", "files/presentations/SAAT_Book.pdf")),
    ])

PROJECTS = [
    dict(cat="robotics", title="Walle (semi-humanoid)", tags=["ROS 2", "Raspberry Pi 4", "ESP32", "Whisper API", "ChatGPT API"],
         text="Walle is a semi-humanoid intelligent robot powered by ROS 2, designed to interact with humans using voice commands and AI-driven decision-making. It integrates multiple actuators, including head and hand servos and wheel motors, to perform complex motions. The robot uses OpenAI's Whisper API for voice-to-text and ChatGPT API for intelligent decision making, providing real-time interactive capabilities. Raspberry Pi 4 and ROS2, ESP32, and Mechanical Design are attached.",
         links=[("GitHub · Walle_ROS2", GH + "Walle_ROS2"), ("GitHub · Walle_ESP32", GH + "Walle_ESP32"), ("Drive folder", DR + "1yA9cazNrOX6GsmrCj_pJwJwgHhN1JA2A?usp=drive_link")], imgs=["p12"]),
    dict(cat="robotics", title="Red Dot Shooter", tags=["ROS 2", "Python", "C++", "PID", "Stepper motors"],
         text="This project integrates robot vision with motor control in ROS 2 for real-time object tracking. A modular set of nodes detects a red object, computes its coordinates, applies inverse kinematics, and uses a PID controller to drive stepper motors. Designed for scalability and industrial use, it supports both Python and C++.",
         links=[("GitHub", GH + "Dot_tracker"), ("Drive folder", DR + "1lKdhMdTtV2ichX0epNMtmYhjj6azN3wQ?usp=drive_link")], imgs=["j1"]),
    dict(cat="robotics", title="FocusOne (Arm Penalization)", tags=["ROS2", "Gazebo", "MoveIt", "SolidWorks", "Matlab", "Ansys"],
         text="A 6-DOF robot is used to manipulate and drive two packages, each weighing 200 kg, from one place to another. In this project, the following tools are used: ROS2, Gazebo, MoveIt, SolidWorks, Matlab, and Ansys.",
         links=[("GitHub", GH + "Focus_one_robot"), ("Drive folder · FocusOne", "https://docs.google.com/folderview?id=1BP6-31T6OjkvcA4aDfHCmaYThleY-10Y")], imgs=["p13", "p54"]),
    dict(cat="robotics", title="MiniPaper", tags=["ROS2", "Mini Pupper", "Reinforcement learning"],
         text="As part of my Robotics Operating Systems (ROS) course with Dr. Li Bai, I completed my first ROS2 project: a line-following mini pupper robot. The project involved using ROS to control the robot’s movement by detecting a black line through its camera and sending precise directions to its servo motors (3 per leg). The hands-on experience in designing and controlling robotic systems has been incredibly rewarding, and I’m excited to build on these skills. Moreover, the paper has become more interactive after integrating reinforcement learning.",
         links=[("LinkedIn post", LI + "george-yaccoup_templeuniversity-robotics-ros2-activity-7256689153940086784-Zsu-"), ("Dr. Li Bai", "https://www.linkedin.com/in/li-bai-86a7814/")], imgs=[]),
    dict(cat="embedded", title="MicroWave Development", tags=["PIC", "RTOS", "SolidWorks", "AutoCAD"],
         text="Using a PIC Microcontroller, using the drivers DIO, PWM, Timer0, Timer1, ADC, and implementing RTOS. Mechanical Design using SolidWorks and AutoCAD. For the embedded software, I utilized various models to enhance my skills in software design and embedded systems, including Digital Input/Output (DIO), UART, ADC, Interrupts, Timer 1, Pulse Width Modulation (PWM). Additionally, I incorporated several components such as LCD, PIC microcontroller, 7-segment display, Keypad, LM36 sensor, Resistors, Push buttons, Heater motors for rotation and cooling, Motor drivers, LEDs.",
         result="Results: vibration 20% lower than local machines, and better software design.",
         links=[("LinkedIn post", LI + "george-yaccoup_pic-embedded-microcontroller-activity-7220053151427514368-cR_g")], imgs=["p16"]),
    dict(cat="embedded", title="Washing Machine Development", tags=["PIC18F4620", "Embedded C", "SolidWorks"],
         text="I designed a complete washing machine system covering mechanical and electrical aspects.",
         bullets=["Electrical Design: Used dual PIC18F4620 microcontrollers, LCD + 7-segment displays, encoders, buttons, LEDs, LM35 sensor, valves, and a 1 HP motor. Implemented drivers for DIO, LCD, UART, ADC, PWM, CCP1, Timer 1, and interrupts.",
                  "Mechanical Design: Included shaft, weldment, pulleys, belts, fasteners, cover, and tank. This multidisciplinary project combined embedded systems with robust mechanical design to deliver an efficient washing machine."],
         links=[("GitHub · Electrical Design", "https://lnkd.in/dvPup8BM"), ("GitHub · Mechanical Design", "https://lnkd.in/dT99Bv6C"), ("LinkedIn post", LI + "george-yaccoup_mechanicalengineering-electricalengineering-activity-7211126841259020288-p3nj")], imgs=["p15", "j4"]),
    dict(cat="embedded", title="PID Autonomous Car", tags=["Arduino Uno", "PID", "MATLAB", "Proteus"],
         text="Microcontroller: Arduino Uno. Controller: PID Control. Application: searching for a specific object and finding it. Input: distance from an ultrasonic sensor controlled by a servo motor. Output: velocity of the vehicle, adjusted based on the distance from the ultrasonic sensor and DC motors, which are controlled by a motor driver L298N. We utilized MATLAB for time-frequency responses and Proteus for simulating the process. A big thank you to everyone who supported and guided me throughout this project!",
         links=[("GitHub", GH + "PID_Autonoums_Car"), ("LinkedIn post", LI + "george-yaccoup_arduino-selfdrivingcar-pidcontrol-activity-7201552893701767170-02rp")], imgs=["j5", "p26"]),
    dict(cat="embedded", title="ATM Software using Qt", tags=["Qt", "C++"], text="ATM software with a graphical interface built using Qt.",
         links=[("GitHub", GH + "ATM_LCD"), ("LinkedIn post", LI + "george-yaccoup_project-design-hardware-activity-7067294257677516800-KxOw")], imgs=["p50"]),
    dict(cat="embedded", title="Students Database", tags=["C", "Embedded"], text="Students database project.",
         links=[("GitHub", GH + "STudentDatabase-"), ("LinkedIn post", LI + "george-yaccoup_cprogramming-embeddedsystems-realtimeoperatingsystems-activity-7072652818100228096--O8a")], imgs=["p51"]),
    dict(cat="embedded", title="AVR Timer", tags=["AVR", "Proteus", "7-segment"], text="AVR timer project using seven-segment displays, simulated in Proteus.",
         links=[("GitHub", GH + "unarranged_pins_7seg/tree/main"), ("LinkedIn post", LI + "george-yaccoup_embeddedsystems-avr-projectshowcase-activity-7081412215840382976-Qts8")], imgs=["p52"]),
    dict(cat="automation", title="Robot Arm two Production Lines", tags=["PLC", "Factory I/O", "Robotic arm"],
         text="Using PLC for automating two assembly lines with a Robotic Arm to displace the products from line 1 to line 2.", links=[("GitHub", GH + "Production_Line_Boxs")], imgs=["p17"]),
    dict(cat="automation", title="Sorting and Assembler Line", tags=["PLC", "Hydraulics", "Robotic arm"],
         text="Using 3 main systems: PLC for automation, Hydraulic Pushers for Sorting, and a Robotic Arm for Assembling products.", links=[("GitHub", GH + "Assembler-")], imgs=["p18"]),
    dict(cat="automation", title="Sorter", tags=["PLC"],
         text="A sorting production line that classifies products according to the size of the box. The project is done mainly using PLC.", links=[("GitHub", GH + "Sorter/tree/main")], imgs=["p19"]),
    dict(cat="automation", title="Color Classifier", tags=["PLC", "Color sensor", "Robotic arms"],
         text="5 production lines were conducted using a sorter and 2 robotic arms, using a color sensor, with a PLC for classifying the products according to their colors.", links=[("GitHub", GH + "Product_color_sorting-")], imgs=["p20"]),
    dict(cat="modelling", title="Humanoid Robot Joint", tags=["Modelling", "Control", "MATLAB"], text="Mechanical drawing and control modelling of a humanoid robot joint.", imgs=["p14", "p25", "p27", "p28", "p29"]),
    dict(cat="modelling", title="Autonomous Self-Driving Car", tags=["Simulink", "Control", "Stability"], text="Modelling and control analysis of an autonomous self-driving car.", imgs=["p21", "p22", "p23", "p24"]),
    dict(cat="modelling", title="Horizontal Wind Turbine", tags=["Simulink", "Modelling"], text="Modelling a horizontal wind turbine.", imgs=["p30", "p31", "p32"]),
    dict(cat="mechanical", title="Sorting and Packaging Pears Machine (SolidWorks)", tags=["SolidWorks"],
         text="Drawing, designing, and assembling my graduation project model. Now, we are working on the manufacturing process.", imgs=["p3", "p33"]),
    dict(cat="mechanical", title="Vision Pears Selecting Mechanics (SolidWorks)", tags=["SolidWorks", "Raspberry Pi 4", "ESP32", "3D printing"],
         text="Drawing, designing, and assembling a mechanism that uses Raspberry Pi 4, Vision Camera, ESP32, and 6 servo motors. I also manufacture this part using 3D printing.", imgs=["p34", "j14"]),
    dict(cat="mechanical", title="Designing and Testing Processor Fins (SolidWorks)", tags=["SolidWorks", "Thermal analysis"],
         text="Drawing and designing computer processor fins, and making the heat stress analysis for testing different types of fin materials and their functionality and failure points.", links=[("Drive folder", DR + "11sZOEk8O-I8Na57mFeqF4bpyZXxpZyyt?usp=sharing")], imgs=["p35", "p36"]),
    dict(cat="mechanical", title="Wheelchair Mechanism for Stairs Climbing (SolidWorks)", tags=["SolidWorks", "Automation"],
         text="The project is also automated to operate automatically without human force.", links=[("Drive folder", DR + "1SldUnhe4A8hiBlvUFlCABiwFRiX6wcqo?usp=sharing")], imgs=["p37"]),
    dict(cat="mechanical", title="Gear Box Design", tags=["SolidWorks"], text="Designing a box that is capable of reducing the force by 20% and increasing the speed by 50%.", imgs=["p38"]),
    dict(cat="mechanical", title="12-Cups Suction Gripper Design and Implementation", tags=["Pneumatics", "Venturi", "3D printing"], text="Design and implementation of a twelve-cup vacuum suction gripper: technical drawing, pneumatic hardware and the assembled gripper plate.", imgs=["j3", "p40", "p59"]),
    dict(cat="mechanical", title="Simulation of Air Resistance on a Big Track using Ansys", tags=["Ansys", "CFD"], text="Air resistance simulation on a big track using Ansys.", imgs=["p41"]),
    dict(cat="mechanical", title="Simulating Aircrafts using Ansys", tags=["Ansys", "CFD"], text="CFD simulation of aircraft airfoils using Ansys.", imgs=["p42", "p43"]),
    dict(cat="mechanical", title="Studying Stress on a Metal Sheet using Ansys APDL", tags=["Ansys APDL", "FEA"], text="Stress study on a metal sheet using Ansys APDL.", imgs=["p44", "p45"]),
    dict(cat="mechanical", title="Simulating and Studying Stress on Railways using SolidWorks and Ansys", tags=["SolidWorks", "Ansys", "FEA"],
         text="This project is being implemented in real life, where I contributed as a Mechanical Engineer. My role focused on performing simulations and conducting mechanical testing for the selected materials and components used in the railway. The railway system is built with 6 main layers, in addition to 3 extra layers that were developed based on the study I conducted over a period of three months.", imgs=["p46", "j6", "j7"]),
    dict(cat="mechanical", title="Designing a Recycling Machine for Hockey Sticks", tags=["SolidWorks", "Control logic"], text="Designed the mechanical and the logical program for a local company working on recycling wooden products.", imgs=["p47"]),
    dict(cat="mechanical", title="Designing a LEGO using Fusion 360", tags=["Fusion 360"], text="Designing a LEGO brick using Fusion 360.", imgs=["p48"]),
    dict(cat="mechanical", title="Working on Injection Molding using Fusion 360", tags=["Fusion 360", "Injection molding"], text="Injection molding simulation using Fusion 360.", imgs=["p49"]),
    dict(cat="mechanical", title="Bottle Opener Manufacturing using CNC Milling", tags=["CNC milling", "MasterCam"], text="Bottle opener manufacturing using CNC milling.", links=[("Drive folder", DR + "1odreHy7SPGT82V80PmbRiI9rwPT33UkK?usp=drive_link")], imgs=["j8"]),
    dict(cat="mechanical", title="Bishop Manufacturing using CNC Turning", tags=["CNC turning", "MasterCam"], text="Chess bishop manufactured using CNC turning.", imgs=["j9"]),
    dict(cat="mechanical", title="Simple Bridge: First Engineering Project", tags=["Structures"], text="My first engineering project: a miniature bridge model.", links=[("LinkedIn post", LI + "george-yaccoup_this-model-is-a-miniature-bridge-or-miniature-activity-6909160142076846080-vlgE")], imgs=["p53"]),
]
PROJECTS_OUTRO = "These are not all the projects I have worked on. I have also completed numerous projects for private clients as well as others that were not formally documented. For further discussion, please feel free to contact me."
MODELLING_NOTE = "On this tab, you will see more about my modelling and control projects. Unfortunately, they are not all of them, as the majority is not documented, but here are insights about what's not listed (I'm still adding the projects)."

# -------------------------------------------------------------- EXPERIENCE
LIN_FAB = LI + "george-yaccoup_internship-fablab-san3atech-activity-7377812568070926337-d8fW"
EXPERIENCE = [
    dict(org="Tech Spot", role="Founder, Instructor", date="JAN 2023 – PRESENT", link=("LinkedIn", LIN_FAB), imgs=["p64", "p61", "p62", "p63"], certs=[],
         paras=["I managed and taught courses in ICDL, Python, C/C++, and Robotics over three years, directly training 125 students from diverse backgrounds, while the academy reached over 400 learners. In response to a government push in 2023 that risked leaving many without jobs due to a lack of computer skills, I transformed my home into a classroom to help older community members overcome their doubts."]),
    dict(org="Fab Lab Egypt", role="Fab Engineer", date="11 Aug – 20 Sep 2025", link=("LinkedIn", LIN_FAB), imgs=["j10", "j12", "j2", "j11"], certs=["p94", "j22"],
         paras=["Working as a Fab Engineer, designing and manufacturing 3D parts using 3D printers, and fabricating models using laser cutters and CNC machines. In addition to working on a humanoid interactive robot that interacts with people to complete tasks and send results to be monitored."]),
    dict(org="HA Consultation Group", role="Internship", date="30 June – 15 Aug 2025", link=("LinkedIn", LI + "george-yaccoup_automation-plc-engineering-activity-7364387170280792064-wPyZ"), imgs=["j13", "j24", "j25", "p65"], certs=["j16", "j23", "j17"],
         paras=["During this internship, the focus was on applying a real-time project using Classic control (designing, simulation using CADe and AKTS, and execution), then turning these designs into a PLC program for better execution and performance, and finally, motor drivers’ selection and usage. On this internship, more than 60 projects were required to be designed and executed. Moreover, executing it on Eplan."]),
    dict(org="DCS (DEVASH Control Systems)", role="Internship", date="JULY 2024", link=("LinkedIn", LI + "george-yaccoup_internshipexperience-devashcontrolsystems-activity-7225974085510430722-Pq5"), imgs=["p66", "p68"], certs=["p67"],
         paras=["Designed electrical panels (HV, MV, LV) and reduced energy waste through digitalization and automation in production processes. Increasing the effectiveness of the panels to more than 83%. Enhanced operational efficiency by analyzing energy systems and collaborating on innovative control solutions. DEVASH Control Systems (DCS) is a Siemens partner in the Elsadat factory. The program provided in-depth training on electric panel design and manufacturing, focusing on both LV (low voltage) and HV (high voltage) panels, as well as automation solutions like SCADA systems and PLCs.",
                "The internship also offered a diverse range of sessions covering topics such as marketing, HR, financials, sales, mechanical and electrical design, and the production process. Beyond the sessions, the site training was invaluable."]),
    dict(org="Siemens", role="Embedded System Intern", date="JUN 2023 – OCT 2023", link=("LinkedIn", LI + "george-yaccoup_siemensinternship-embeddedsoftwaredevelopment-activity-7132480367860588544-A4Sr"), imgs=[], certs=["p69", "p90"],
         paras=["Programmed embedded systems with AVR and ARM microcontrollers, leveraging Siemens RTOS and AUTOSAR for efficient rail automation and electrification solutions. We worked on one method for reducing the response time to less than 1 microsecond. Collaborated with a multidisciplinary team to innovate intelligent mobility solutions, emphasizing digitalization and performance optimization."]),
    dict(org="ExxonMobil", role="Internship", date="27 Aug 2023 – 30 Sept 2023", link=("LinkedIn", LI + "george-yaccoup_internshipexperience-exxonmobil-usaid-activity-7116168628273606656-nNyk"), imgs=["p70", "p72"], certs=["p91"],
         paras=["Reflecting on an incredible internship experience with ExxonMobil Egypt this September, where I gained both personal and professional growth across multiple locations:"],
         bullets=["10th of Ramadan: Hands-on exposure to operations in a dynamic environment.", "Mostorod Terminal: Learned about critical processes in energy production and distribution.", "Alexandria: Contributed to meaningful projects and collaborated with talented professionals for two weeks."],
         after="This journey provided me with invaluable skills, industry insights, and mentorship that will shape my future career."),
    dict(org="Halliburton", role="Sperry Drilling Department", date="Aug 2023", link=("LinkedIn", LI + "george-yaccoup_halliburtoninternship-sperrydrilling-lwd-activity-7097953915207323648-C0U2"), imgs=["p71", "p73", "p74"], certs=["p89"],
         paras=["I am pleased to share that I have successfully completed my internship at Halliburton in the Sperry Drilling Department. During this journey, I gained hands-on experience across three key areas:"],
         bullets=["LWD (Logging While Drilling): Real-time formation evaluation using advanced subsurface data analysis.", "MWD (Measurements While Drilling): Insights into downhole measurements and their role in optimizing drilling operations.", "iCruise: Exposure to drilling automation and software tools for improving operational efficiency."],
         after="I am deeply grateful to USAID and Halliburton for this opportunity, and to my mentor Eng. George Baher and my colleagues. This internship has been invaluable in enhancing my technical skills, professional growth, and passion for the energy sector."),
    dict(org="SemiColon", role="Training program", date="July 2023", link=("LinkedIn", LI + "george-yaccoup_halliburtoninternship-sperrydrilling-lwd-activity-7097953915207323648-C0U2"), imgs=["p75"], certs=[],
         paras=["Experience with SemiColon in AVR (ATmega32) and ARM (STM32) microcontroller programming, held in Cairo this August. The program covered a wide range of topics:"],
         bullets=["AVR: DIO, seven-segment display, LCD, ADC, interrupts, timers, UART, SPI, I2C", "ARM: DIO, NVIC, RTOS, Systick Timer"],
         after="This hands-on training provided me with practical experience and deeper knowledge in embedded systems, strengthening my skills in microcontroller programming."),
]

# ------------------------------------------------------------------ SKILLS
SKILLS = [
    ("Electrical Engineering", "bolt", ["Electrical Design and Simulation", "PCB design using Altium, Proteus, and KiCad", "Simulation and Testing PCB", "Designing Electrical Circuits"]),
    ("Mechanical Design and Simulation", "gear", ["Mechanical Design Programs: SolidWorks, Ansys (Fluent and Mechanical, APDL), AutoCAD, Fusion", "HVAC and Heat Transfer using Ansys & HAP", "CNC programming and designing using MasterCam"]),
    ("Programming Languages", "code", ["Python, C/C++, Java, MySQL, Embedded C", "MATLAB, Qt-Creator, and LabView", "OpenCV and Image Processing"]),
    ("Embedded Systems Design", "chip", ["Arduino, AVR, PIC, and ARM microcontrollers usage", "RTOS and AUTOSAR implementation"]),
    ("Robotics", "robot", ["ROS2 using Python and C++", "Robotics Platforms: ESP32, Arduino, Raspberry Pi 4 & 5, NVIDIA Jetson Nano", "RViz, Gazebo, and MuJoCo simulation, and a perfect understanding of URDF, XML and its writing", "Strong understanding of Robot Kinematics, Dynamics, Trajectory Generation, and Path planning techniques like A*, RRT, and RRT*"]),
    ("AI and ML", "brain", ["Good understanding of reinforcement learning", "Good understanding of Linear and logistic regression, and neural networks"]),
    ("Automation Systems Design and Classic Control", "plc", ["Excellent understanding of Classic control, with simulation using CADe and AKTS", "Good understanding of PLC programming, with simulation using LogixPro, TIA, and Factory I/O", "Panel building using Eplan"]),
]
NONTECH = ["Very Good Team player and Team Leader.", "Research-oriented Mindset.", "Handworker and Dedicated Researcher.", "Resistance and Growth Mindset."]

# ---------------------------------------------------------------- COMMUNITY
COMMUNITY = [
    dict(org="Matrix Mu", role="Mentor", paras=["Over the past two years, I have guided 60 students in mastering embedded systems. Many of them now hold strong roles in leading companies, while others support me in teaching and mentoring their peers. I also coached a group that achieved 1st place in the Creativa competition last summer. In addition, I trained another 30 students in this field."], imgs=["j15"]),
    dict(org="Green Assiut University Initiative", role="HR Leader and Program Coordinator", paras=["During two cohorts of this program, we trained around 200 students to understand and integrate sustainable solutions in their lives, and each one of them knows how important it is to live in a sustainable way. Lots of them lead others to learn about SDGs, and others become partners on the program. I worked as HR Leader and Program Coordinator."], imgs=["p77", "p78"]),
    dict(org="Enactus AU", role="HR Leader", paras=["For two years, I worked as HR Leader for more than 50 students, teaching them how to complete tasks and work on many projects without affecting other projects. Also, I worked on a new evaluation criterion that helped the team to win competitions and compete globally and locally."], imgs=[]),
    dict(org="ASME AU", role="Monitor and Technical Team Member", paras=["ASME is one of the international student activities that supports students to participate in international competitions like XRC and other competitions. I worked as a monitor and technical team member."], imgs=["p79"]),
    dict(org="Assiut Robotics", role="Team Member · ROV", paras=["Assiut Robotics gave me the kick start to my career, they allowed me to work on ROV, and another project that allowed me to get deeper into my field of study and myself, I learned how to learn and act on a team, and learning topics like C programming, Electronics, Electrical Design, ROS, and Embedded Systems.",
                                                                                          "One of my proudest achievements is participating in my first ROV competition during my freshman year. I learned ROS in just one month to prepare for the competition, and our team secured 3rd place."], imgs=["p80", "p81"]),
    dict(org="USAID Scholars Camps", role="Head of Volunteers", paras=["Through 3 winters and summer camps, I worked with 5 other leaders, facilitating transportation, food, accommodation, and logistics for more than 140 students at the same place, coordinating that with monitors and scholarship managers."], imgs=["p82"]),
]

# ------------------------------------------------------------ PRESENTATIONS
PRES_FILES = ["Forsaken Places Portfolio by Slidesgo.pptx", "Robotics Recreations.pdf", "Robot Vision.pptx", "AI_Chatting.pptx", "Final Presesntation.pdf", "AI chatting.pptx",
              "Supply-Chain.pptx", "Lean Manufacturing.pptx", "903139_Conferance Presentation.pptx", "Pneumatic_Gripper_Systems_Engineering.pdf", "MicroRobotics.pptx", "presentation.pptx",
              "interactive-corporate-interface-for-business.pptx", "titan.pptx", "Computers.pptx", "Happy World Water life.pptx", "Processors-Vs-Human-Brains.pptx", "Vehicles.pptx",
              "pepper.pptx", "Wind.pptx", "What-are-Wind-Turbines.pptx", "Final_Presesntation.pdf", "presentation_sensors_V2.pptx"]

# ------------------------------------------------------------------- COURSES
TRANSCRIPT = ("unofficial transcript - George Read.pdf", "files/courses/unofficial transcript - George Read.pdf")
COURSES_IMGS = ["p86", "p85"]

# ------------------------------------------------------------- CERTIFICATES
CERTS = [
    ("IEEE Egypt AP-S / MTT-S: Certificate of Excellence", "IC-FTA, Nov 2025", ["p1", "p92"]),
    ("HA Consulting Group: Classic Control", "2025", ["j16"]),
    ("HA Consulting Group: PLC Basic Programming", "2025", ["j23"]),
    ("HA Consulting Group: Electric Motor & Drive Programming", "2025", ["j17"]),
    ("Fab Lab Egypt (SanaTech): Internship", "Sept 2025", ["p94", "j22"]),
    ("Siemens: Developing Embedded Software with Adaptive AUTOSAR", "2023", ["p69", "p90"]),
    ("DCS: LV, MV & HV Automation Internship Program", "2024", ["p67"]),
    ("ExxonMobil: One-week internship", "Sept 2023", ["p91"]),
    ("Halliburton: Training certificate", "Aug 2023", ["p89"]),
    ("AMIT: Embedded Systems Diploma (Grade 95%)", "2023", ["p85"]),
    ("University of Alberta (Coursera): Fundamentals of Reinforcement Learning", "", ["p84"]),
    ("Udacity: Introducing Generative AI with AWS", "July 2025", ["p93"]),
    ("SolidWorks: Mechanical Design", "Nov 2023", ["p95"]),
    ("VR Course: Certificate of Achievement", "Aug 2023", ["j21", "p76"]),
    ("AUC: Supplemental English Language Program 1", "2022", ["j18", "j26"]),
    ("AUC: Supplemental English Language Program 2", "2022–2023", ["j19"]),
    ("Dialogue workshop: Certificate of Appreciation", "5-3-2023", ["j20"]),
    ("USAID Scholars: Aspire Leadership and Skills Development Program", "2023–2024", ["p83"]),
    ("USAID Scholars: Annual Entrepreneurship Summit 2022", "Sept 2022", ["p87"]),
    ("USAID Scholars: Venture Progress Pitch (Frozen Minds)", "July 2024", ["p88"]),
]

# Photos that were taken sideways: degrees to rotate counter-clockwise (negative = clockwise)
ROTATE = {"j16": 90, "j17": 90, "j23": 90, "j22": -90}
