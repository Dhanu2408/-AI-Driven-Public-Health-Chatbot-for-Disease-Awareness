AI-Driven Public Health Chatbot for Disease Awareness

                                            Requirement Gathering
1. Project Overview

The AI-Driven Public Health Chatbot for Disease Awareness is designed to provide users with instant, reliable health-related information about diseases, symptoms, prevention methods, and first-aid guidance. It uses AI/NLP techniques to interact with users in a conversational manner and improve public health awareness.

2. Objectives
Provide quick access to disease-related information
Increase public awareness about common and seasonal diseases
Offer preventive care suggestions
Reduce dependency on manual health information searches
Support users with basic health guidance in real time

3. Stakeholders
End Users: General public seeking health information
Healthcare Organizations: Hospitals, NGOs, health departments
Developers: AI/chatbot system developers
Administrators: System maintainers and data updaters

4. Functional Requirements

The system should be able to:

Accept user input in natural language (chat format)
Identify disease-related queries using NLP
Provide information about:
Symptoms of diseases
Causes and transmission methods
Preventive measures
Basic first-aid suggestions
Suggest when to consult a doctor
Handle frequently asked health questions
Support multiple user queries in conversation flow
Provide responses quickly and accurately
Maintain conversation context (basic session handling)

5. Non-Functional Requirements
Performance: Responses should be generated within a few seconds
Accuracy: Information must be reliable and medically validated
Usability: Simple and user-friendly chat interface
Scalability: Should support multiple users simultaneously
Security: No personal medical data should be stored without consent
Availability: System should be accessible 24/7
Maintainability: Easy to update disease database and AI model

6. Hardware Requirements
Processor: i3 or higher (recommended i5/i7)
RAM: Minimum 4GB (8GB preferred for AI processing)
Storage: 500MB–2GB depending on dataset
Internet connection (for API-based chatbot or cloud model)

7. Software Requirements
Python (3.8+)
NLP libraries (NLTK / spaCy)
Machine Learning libraries (Scikit-learn / TensorFlow if used)
Flask / Django (for web chatbot interface)
Database (SQLite / MySQL / Firebase)
Frontend: HTML, CSS, JavaScript (if web-based)

8. User Requirements
Users should be able to type health-related questions easily
No technical knowledge required
System should respond in simple language

                                  Objective – AI-Driven Public Health Chatbot for Disease Awareness

The main objective of the AI-Driven Public Health Chatbot for Disease Awareness project is to develop an intelligent conversational system that provides users with quick, accurate, and easy-to-understand information about various diseases and health-related topics.

This chatbot aims to improve public health awareness by assisting users in understanding disease symptoms, causes, prevention methods, and basic first-aid guidance through natural language interaction. It reduces the need for manual searching of medical information and provides instant responses to health queries.

The system also helps guide users on when to seek professional medical help, ensuring safe and responsible usage of health information. Overall, the objective is to make healthcare awareness more accessible, interactive, and efficient using AI and Natural Language Processing technologies. 

                                                User and Module Identification
AI-Driven Public Health Chatbot for Disease Awareness
1. User Identification

The system is designed to serve the following types of users:

1. General Users (Public Users)
Individuals seeking information about diseases and health awareness
Can ask queries related to symptoms, prevention, and basic first aid
No technical knowledge required
Primary users of the chatbot system
2. Healthcare Awareness Seekers
Students, researchers, or health workers
Use the chatbot for quick reference and disease-related information
Access structured medical awareness content
3. System Administrator
Responsible for managing chatbot data and system performance
Updates disease information and improves response quality
Maintains system security and accuracy
2. Module Identification

The system is divided into the following major modules:

1. User Interaction Module
Provides a chat interface for user communication
Accepts natural language input from users
Displays chatbot responses in real time

2. Natural Language Processing (NLP) Module
Processes and understands user queries
Identifies intent such as symptoms, prevention, or disease information
Converts user input into machine-understandable format

3. Disease Knowledge Base Module
Stores structured information about diseases
Includes symptoms, causes, prevention, and awareness details
Acts as the primary data source for chatbot responses

4. AI Response Generation Module
Generates appropriate responses based on user queries
Matches input with knowledge base or AI model output
Ensures accurate and simple health-related answers

5. Recommendation and Awareness Module
Suggests preventive measures
Provides health awareness tips
Advises users when medical consultation is required
6. Database Management Module
Stores user queries (optional)
Maintains disease datasets and chatbot logs
Supports system improvement and optimization

7. Admin Module
Allows admin to update disease information
Monitors chatbot performance
Ensures system security and content accuracy

                                              UML Diagram Design
AI-Driven Public Health Chatbot for Disease Awareness

The system architecture is represented using multiple UML diagrams to clearly describe user interaction, system behavior, data flow, and deployment structure.

1. Use Case Diagram
Actors:
User
Admin
Use Cases:
Ask Health Query
Get Disease Information
Get Symptoms Details
Get Prevention Tips
Get First Aid Guidance
Know When to Consult a Doctor
Provide Feedback
Manage Disease Database (Admin)
Update System Content (Admin)
Description:

The use case diagram represents how users interact with the chatbot system. The user can access disease-related information, while the admin manages and updates the system knowledge base.

2. Class Diagram
Main Classes:

User

userId
name
email
Methods:
register()
login()
sendQuery()

Chatbot

botId
modelType
Methods:
getResponse()
processQuery()

NLPProcessor

tokenizer
intentClassifier
entityExtractor
Methods:
preprocess()
detectIntent()
extractEntities()

KnowledgeBase

diseaseData
symptomData
preventionData
Methods:
searchData()
getDiseaseInfo()

ResponseGenerator

templateEngine
Methods:
generateResponse()
formatResponse()

Admin

adminId
name
Methods:
login()
addDisease()
updateDisease()
deleteDisease()

3. Activity Diagram
Flow:
User sends query
System preprocesses input (NLP)
Intent and entities are extracted
System searches knowledge base
If data found → generate response
If not found → suggest consulting doctor
Response is sent to user
Feedback is optionally stored

4. Sequence Diagram
Participants:
User
Chatbot Interface
NLP Processor
Knowledge Base
Response Generator
Database

Flow:
User sends message
Chatbot interface receives input
NLP processor analyzes query
Knowledge base is searched
Response generator formats answer
Final response is sent to user
Feedback stored in database (optional)

5. Deployment Diagram
Components:

User Device

Web/Mobile Chat Interface

Application Server

Chatbot Application (Flask/Django)
NLP & ML Model
Response Generator

Database Server

Disease Knowledge Base (MySQL/SQLite/Firebase)
Architecture Flow:

User Device → Application Server → Database Server → Response returned to User Device

                                                         Database Requirement Analysis

A Database Requirement Analysis for the AI-Driven Public Health Chatbot for Disease Awareness project ensures the system can securely, rapidly, and accurately handle multi-modal healthcare data. Because public health platforms rely on verified knowledge bases, conversational histories, and location-based alerts, a polyglot persistence model (combining Vector, Relational, and NoSQL databases) is required

1. Data Requirements & ClassificationsThe architecture must support four primary types of data storage and access patterns:
2. Knowledge Base Data (Unstructured to Vector): Verifiable medical datasets (e.g., WHO guidelines, MoHFW publications, medical ontologies) used for Retrieval-Augmented Generation (RAG).
3. Conversational Data (Semi-Structured): Real-time chat logs, message time stamps, session tokens, multi-language message states, and user context vectors.
4. Operational & User Data (Structured): User profiles, multi-lingual language preferences, location metadata for disease clustering, and vaccination tracking logs.
5. Analytics & Public Health Metrics (Time-Series/Relational): Aggregated symptom search trends, geographic outbreak tracking, and bot evaluation telemetry (e.g., feedback ratings).
6. Conceptual Database ArchitectureA single database engine cannot meet these disparate AI and administrative demands efficiently.

7. Core Functional Entity Requirements (Schema Outlines)

A. Vector Layer (Knowledge Base Index)ID: Unique identifier for the document chunk.Vector Values: Float arrays (e.g., 1536 dimensions for OpenAI or 384 for Hugging Face embeddings).Metadata: {"source": "WHO_2026_Dengue_Doc", "disease": "Dengue", "language": "Hindi", "category": "Prevention"}.
B. Conversational Layer (NoSQL Collections)Session ID: Unique identifier for the specific conversation thread.User ID: Reference back to the operational database.Messages Array:Timestamp: ISO standard time format.Sender: User or AI-Bot.Content: Text string or multi-modal image references.Language: Detected user language code (e.g., en, hi, te).
C. Operational & Public Health Analytical Layer (Relational Tables)Users Table: user_id (PK), demographics, preferred_language, created_at.Symptom_Logs Table: log_id (PK), user_id (FK), detected_symptoms (Array), predicted_disease_category, geolocation_lat_long, logged_at.Alerts Table: alert_id (PK), region_code, disease_type, severity_level, published_at.

8. Non-Functional Database RequirementsLow Latency & High Throughput: The vector database must return top-k semantic search matches within milliseconds to achieve a targeted total chatbot response time under 2 to 3 seconds.Strict Healthcare Compliance & Privacy: Encryption of personally identifiable information (PII) at rest and in transit using AES-256 and TLS 1.3.
To secure health tracking information, the system must separate anonymous symptom logs from identifiable user records.
Data Synchronization & Offline Availability: The database layer must support schema sync for cached user inputs when the chatbot is operating in an offline-first format via lightweight client-side engines like SQLite or Hive.Scalability: Automatic partitioning/sharding to manage millions of message interactions during seasonal disease outbreaks or public health emergencies.


                                                    Entities and Attributes
1. User
User_ID (Primary Key)
Name
Age
Gender
Email
Phone_Number
Location
Registration_Date
2. Chatbot
Bot_ID (Primary Key)
Bot_Name
Version
Language_Supported
Last_Updated
3. Disease
Disease_ID (Primary Key)
Disease_Name
Category
Symptoms
Causes
Prevention_Methods
Treatment_Information
4. Awareness_Content
Content_ID (Primary Key)
Title
Description
Content_Type
Publish_Date
Disease_ID (Foreign Key)
5. Health_Query
Query_ID (Primary Key)
User_ID (Foreign Key)
Query_Text
Query_Date
Query_Status
6. Chat_Response
Response_ID (Primary Key)
Query_ID (Foreign Key)
Bot_ID (Foreign Key)
Response_Text
Response_Time
7. Feedback
Feedback_ID (Primary Key)
User_ID (Foreign Key)
Response_ID (Foreign Key)
Rating
Comments
Feedback_Date
8. Health_Alert
Alert_ID (Primary Key)
Disease_ID (Foreign Key)
Alert_Message
Alert_Date
Severity_Level
Relationships
User submits Health_Query
One User → Many Health_Queries
(1 : M)
Health_Query receives Chat_Response
One Query → One or Many Responses
(1 : M)
Chatbot generates Chat_Response
One Chatbot → Many Responses
(1 : M)
Disease contains Awareness_Content
One Disease → Many Awareness Contents
(1 : M)
Disease triggers Health_Alert
One Disease → Many Alerts
(1 : M)
User provides Feedback
One User → Many Feedbacks
(1 : M)
Chat_Response receives Feedback
One Response → Many Feedbacks
(1 : M)
ER Diagram Flow (Words Only)

User → submits → Health_Query → processed by → Chatbot → generates → Chat_Response

Disease → provides → Awareness_Content

Disease → generates → Health_Alert

User → gives → Feedback → for → Chat_Response

                                                    Database schema creation

The database schema for the AI-Driven Public Health Chatbot for Disease Awareness project consists of eight main tables that store user information, disease details, chatbot interactions, awareness content, feedback, and health alerts.

1. User Table

The User table stores the details of people who interact with the chatbot. It contains attributes such as User ID, Name, Age, Gender, Email Address, Phone Number, Location, and Registration Date. The User ID acts as the primary key and uniquely identifies each user.

2. Chatbot Table

The Chatbot table contains information about the chatbot system. It includes Bot ID, Bot Name, Version, Supported Languages, and Last Updated Date. The Bot ID serves as the primary key for identifying the chatbot.

3. Disease Table

The Disease table stores information related to various diseases. It contains Disease ID, Disease Name, Category, Symptoms, Causes, Prevention Methods, and Treatment Information. The Disease ID uniquely identifies each disease in the system.

4. Awareness Content Table

The Awareness Content table stores educational and awareness-related materials about diseases. It contains Content ID, Title, Description, Content Type, Publish Date, and Disease ID. The Disease ID acts as a foreign key linking awareness content to a specific disease.

5. Health Query Table

The Health Query table records the questions asked by users. It contains Query ID, User ID, Query Text, Query Date, and Query Status. The User ID acts as a foreign key that connects each query to the corresponding user.

6. Chat Response Table

The Chat Response table stores responses generated by the chatbot. It contains Response ID, Query ID, Bot ID, Response Text, and Response Time. Query ID and Bot ID are foreign keys used to establish relationships with the Health Query and Chatbot tables.

7. Feedback Table

The Feedback table stores user opinions and ratings about chatbot responses. It contains Feedback ID, User ID, Response ID, Rating, Comments, and Feedback Date. User ID and Response ID are foreign keys linking feedback to both the user and the chatbot response.

8. Health Alert Table

The Health Alert table stores disease-related alerts and notifications. It contains Alert ID, Disease ID, Alert Message, Alert Date, and Severity Level. Disease ID acts as a foreign key connecting alerts to the corresponding disease.

                                                     UI Wireframe Design Prompt

Title: AI-Driven Public Health Chatbot for Disease Awareness

Design Style: Clean, modern healthcare dashboard with blue and green color theme, mobile-responsive layout.

Screen 1: Home Page
Header with:
Project Logo
Project Name
Navigation Menu (Home, Disease Info, Chatbot, Awareness, Contact)
Hero Section:
Welcome message: "AI-Driven Public Health Chatbot for Disease Awareness"
Short description about disease awareness and public health education
"Start Chat" button
Features Section:
Disease Information
Symptom Awareness
Health Tips
AI Chat Assistance
Footer:
Contact Information
Privacy Policy
Social Media Icons

Screen 2: User Login / Registration
Login Form
Email
Password
Login Button
Registration Form
Name
Email
Mobile Number
Password
Register Button

Screen 3: AI Chatbot Interface
Header:
Chatbot Name
User Profile Icon
Left Sidebar:
Chat History
Saved Conversations
Disease Categories
Main Chat Area:
User Messages
AI Responses
Typing Indicator
Bottom Input Area:
Message Text Box
Voice Input Button
Send Button

Screen 4: Disease Awareness Module
Search Bar
Disease Categories:
COVID-19
Dengue
Diabetes
Hypertension
Malaria
Information Card:
Disease Name
Symptoms
Causes
Prevention
Treatment Suggestions

Screen 5: Health Tips Dashboard
Daily Health Tips Section
Preventive Measures Cards
Nutrition Recommendations
Exercise Recommendations
Vaccination Awareness Section

Screen 6: Admin Dashboard
Sidebar:
Dashboard
Manage Diseases
Manage Awareness Content
User Management
Reports
Main Dashboard:
Total Users
Total Chat Sessions
Disease Searches
Awareness Campaign Statistics
Charts:
User Activity Graph
Disease Query Trends
Monthly Usage Report

                                                     Login and Dashboard Design
Overview

The Login and Dashboard modules were developed to provide secure access and a user-friendly experience for the AI-Driven Public Health Chatbot for Disease Awareness. These interfaces serve as the primary entry point for users and help them easily navigate through the chatbot system.

Login Page Design

The Login Page is designed to authenticate users before accessing the chatbot features. The interface is simple, responsive, and easy to use.

Features Implemented
User Email Input Field
Password Input Field
Login Button
Form Validation
Responsive Design
User-Friendly Interface
Purpose

The login page ensures that only registered users can access the chatbot services. It acts as a secure gateway to the application and provides a smooth user authentication experience.

Design Highlights
Clean healthcare-themed layout
Simple navigation structure
Easy-to-read labels and input fields
Mobile-friendly and responsive design
Dashboard Design

The Dashboard serves as the main user interface after successful login. It provides quick access to chatbot features and disease awareness resources.

Features Implemented
Welcome Section for Users
Navigation Menu
Quick Access to Chatbot
Disease Awareness Information Section
Health Tips and Guidance Area
User-Friendly Layout
Responsive Dashboard Design
Purpose

The dashboard acts as the central control panel of the system. It allows users to easily navigate between different sections and access health-related information efficiently.

Dashboard Components
Home Section

Displays a welcome message and provides an introduction to the chatbot system.

Chatbot Access

Allows users to start interacting with the AI chatbot and ask disease-related questions.

 Disease Information Section

Provides awareness content related to symptoms, causes, prevention methods, and treatment information for various diseases.

Health Tips Section

Displays preventive healthcare tips and awareness recommendations for maintaining good health.

Navigation Panel

Provides easy access to all major modules within the system.

Benefits of the Login and Dashboard Design
Provides secure access to the application.
Enhances user experience through a simple interface.
Allows quick navigation between modules.
Improves accessibility for users with minimal technical knowledge.
Supports responsive viewing across desktop and mobile devices.
Creates a professional and organized healthcare application environment.

                                                          Navigation and Form Design
Overview

The Navigation and Form Design module was developed to ensure smooth interaction between users and the AI-Driven Public Health Chatbot for Disease Awareness system. A well-structured navigation system helps users move easily between different sections of the application, while properly designed forms allow users to submit information efficiently and accurately.

The primary goal of this module is to provide a simple, intuitive, and user-friendly interface that can be easily used by people with little or no technical knowledge.

Navigation Design

The navigation structure was designed to provide quick access to all major features of the chatbot system. The navigation menu helps users move between different pages without confusion and improves the overall user experience.

Features Implemented
Home Page Navigation
Chatbot Access Page
Disease Information Section
Health Tips Section
Contact Page
Login and Registration Pages
Dashboard Navigation
Navigation Menu Components
Home

The Home page serves as the landing page of the application. It introduces users to the purpose of the chatbot and provides access to key features.

Chatbot

This section allows users to interact directly with the AI chatbot and ask health-related questions.

Disease Information

Provides awareness content about various diseases, including symptoms, causes, prevention methods, and treatment guidance.

Health Tips

Displays health recommendations, preventive measures, and wellness suggestions to promote public health awareness.

Contact

Allows users to access support information and communicate with system administrators if required.

Login/Register

Provides authentication options for users to securely access the application.

Form Design

Forms were designed to collect user information and health-related queries in a structured manner. The forms were kept simple, responsive, and easy to understand.

Objectives of Form Design
Collect user information accurately
Provide easy interaction with the chatbot
Reduce user input errors
Improve usability and accessibility
Login Form

The Login Form allows registered users to access the chatbot system.

Fields Included
Email Address
Password
Login Button
Features
Required field validation
User-friendly layout
Responsive design
Error handling for invalid inputs
Registration Form

The Registration Form allows new users to create an account within the system.

Fields Included
Full Name
Email Address
Mobile Number
Password
Confirm Password
Features
Input validation
Password confirmation check
User-friendly interface
Responsive design
Health Query Form

The Health Query Form is the core interaction component of the chatbot system.

Fields Included
Query Input Text Box
Send Button
Features
Accepts disease-related questions
Supports natural language input
Simple and interactive design
Quick submission process
Example Queries
What are the symptoms of dengue?
How can I prevent malaria?
What should I do if I have a fever?
Disease Management Form (Admin)

This form is used by administrators to manage disease-related information stored in the system.

Fields Included
Disease Name
Symptoms
Causes
Prevention Methods
Treatment Information
Features
Add new disease records
Update existing information
Delete outdated records
View stored disease data

                                                  Design Overview
Overview

The AI-Driven Public Health Chatbot for Disease Awareness is designed as a user-friendly and intelligent healthcare awareness platform that provides users with instant access to disease-related information through a conversational chatbot interface. The system combines Artificial Intelligence (AI), Natural Language Processing (NLP), frontend technologies, and backend services to deliver accurate and reliable health awareness information.

The overall design focuses on simplicity, accessibility, responsiveness, and efficiency, ensuring that users can easily interact with the system regardless of their technical knowledge. The architecture is modular, allowing different components to work independently while maintaining seamless communication throughout the application.

System Design Approach

The system follows a layered architecture consisting of:

1. Presentation Layer (Frontend)

The presentation layer is responsible for user interaction. It provides a clean and responsive interface through which users can access chatbot services, disease information, and health awareness content.

Components:

Home Page
Login Page
Registration Page
User Dashboard
Chatbot Interface
Disease Information Page
Health Tips Section

Technologies Used:

HTML
CSS
JavaScript
2. Application Layer (Backend)

The application layer processes user requests and manages system functionality. It acts as the bridge between the frontend and the database.

Responsibilities:

Processing user queries
Managing chatbot logic
Handling user authentication
Communicating with the database
Generating responses

Technology Used:

Spring Boot
3. Data Layer (Database)

The data layer stores and manages all information required by the system.

Data Stored:

User information
Disease details
Chat history
Health awareness content
Feedback records

Database Used:

MySQL / SQLite
User Interface Design

The user interface is designed with a healthcare-oriented theme using clean layouts and intuitive navigation.

Design Goals
Simple and easy to use
Mobile responsive
Fast navigation
Professional appearance
Accessible to all users
Key UI Components
Navigation Bar
Login and Registration Forms
Chat Interface
Dashboard
Disease Information Cards
Health Tips Section
Chatbot Design

The chatbot is the core component of the project. It is designed to interact with users using natural language and provide disease awareness information.

Chatbot Functions
Accept user health-related questions
Identify user intent
Retrieve relevant disease information
Generate appropriate responses
Provide awareness and prevention guidance
Example Interaction

User: What are the symptoms of dengue?

Chatbot: Common symptoms of dengue include fever, headache, muscle pain, joint pain, skin rash, and fatigue. If symptoms become severe, consult a healthcare professional immediately.

Navigation Design

The navigation system allows users to move smoothly between different modules of the application.

Navigation Menu
Home
Chatbot
Disease Information
Health Tips
Contact
Login/Register

The navigation structure was designed to reduce complexity and improve accessibility.

Form Design

Various forms are included to collect and process user information.

Forms Included
Login Form
Registration Form
Health Query Form
Disease Management Form (Admin)

The forms include validation mechanisms to ensure accurate data entry and improved user experience.

                                                Frontend Environment Setup
Overview

The Frontend Environment Setup phase focused on preparing the development environment required to build the user interface of the AI-Driven Public Health Chatbot for Disease Awareness. The frontend is responsible for providing an interactive and user-friendly platform where users can access disease awareness information, communicate with the chatbot, and navigate through different modules of the application.

The objective of this phase was to establish a structured and organized development environment that supports efficient UI development, easy maintenance, and future scalability.

Purpose of Frontend Setup

The frontend environment was set up to achieve the following objectives:

Create a responsive and user-friendly interface
Enable smooth interaction between users and the chatbot
Organize project files systematically
Support easy development and testing
Ensure compatibility across different devices and browsers

This setup acts as the foundation for all frontend development activities carried out in later stages of the project.

Technologies Used

The frontend of the project was developed using standard web technologies:

HTML (HyperText Markup Language)

HTML was used to create the structure of web pages such as the Home Page, Login Page, Registration Page, Dashboard, and Chatbot Interface.

CSS (Cascading Style Sheets)

CSS was used to design and style the user interface. It helped improve the visual appearance of the application by adding colors, spacing, layouts, and responsive design elements.

JavaScript

JavaScript was used to add interactivity to the application, including button actions, form validation, dynamic content updates, and chatbot interaction features.

Development Tools

The following tools were used to create and manage the frontend environment:

Visual Studio Code (VS Code)

VS Code was used as the primary code editor because of its simplicity, extensions, and debugging support.

Live Server Extension

The Live Server extension was used to run and test web pages locally during development. It automatically refreshed the browser whenever changes were made to the code.

Web Browser

Google Chrome was used for testing and debugging the frontend interface.

Project Folder Structure

A structured folder hierarchy was created to organize project files efficiently.

AI_Public_Health_Chatbot/
│
├── index.html
├── login.html
├── register.html
├── dashboard.html
├── chatbot.html
│
├── css/
│   └── style.css
│
├── js/
│   └── script.js
│
├── images/
│   └── logo.png
│
└── assets/

This structure improves maintainability and makes future modifications easier.

User Interface Preparation

The frontend environment was configured to support the development of multiple user interface components.

Home Page

Created the main landing page that introduces the project and provides access to major features.

Login Page

Prepared a secure user authentication interface.

Registration Page

Designed a user registration form for new users.

Dashboard

Created a central navigation page where users can access chatbot services and disease awareness information.

Chatbot Interface

Prepared the main interaction area where users can communicate with the AI chatbot.

Responsive Design Setup

Special attention was given to ensuring that the application works properly on different devices.

Features Implemented
Mobile-friendly layouts
Flexible page structures
Adaptive screen sizing
Cross-browser compatibility

The responsive setup ensures that users can access the system from desktops, tablets, and smartphones without usability issues.

Styling Configuration

A healthcare-themed visual design was selected for the project.

Color Theme
Blue: Represents trust and reliability
Green: Represents health and wellness
White: Provides clarity and readability
Design Elements
Clean layout structure
Consistent typography
Proper spacing and alignment
User-friendly navigation components

These design choices help create a professional healthcare-oriented interface.

Testing Environment Setup

The frontend environment was tested continuously during development.

Testing Activities
Checking page loading functionality
Verifying navigation links
Testing form validation
Ensuring responsive behavior
Identifying and fixing UI issues

This helped maintain a stable and functional user interface throughout development.

Benefits of Frontend Environment Setup
Organized project development
Faster implementation of UI components
Easier debugging and testing
Improved code maintainability
Better user experience
Scalability for future enhancemet

                                             Login Page Development
Overview

The Login Page Development phase focused on creating a secure and user-friendly authentication interface for the AI-Driven Public Health Chatbot for Disease Awareness. The login page acts as the entry point to the application and allows registered users to access the chatbot services, disease awareness content, and personalized features of the system.

The primary objective of this phase was to design a simple, responsive, and efficient login interface that ensures a smooth user experience while maintaining basic security and authentication standards.

Purpose of the Login Page

The login page serves as the gateway to the application. It verifies user credentials before granting access to the system and ensures that only authorized users can utilize the chatbot and other platform features.

The login functionality helps in:

Authenticating registered users
Protecting system resources from unauthorized access
Managing user sessions
Providing personalized access to services
Enhancing overall system security
Design Objectives

The login page was designed with the following goals:

Simplicity and ease of use
Clean and professional healthcare-themed interface
Fast and secure authentication process
Responsive design for multiple devices
Easy navigation to registration and dashboard pages

Special attention was given to ensuring that users of all age groups can easily understand and use the interface.

User Interface Design

The login page follows a simple and structured layout.

Main Components
Project Title Section

Displays the project name:

AI-Driven Public Health Chatbot for Disease Awareness

This section introduces the application and provides context to users.

Email Input Field

Allows users to enter their registered email address.

Purpose:

Identifies the user account
Acts as the primary login credential
Password Input Field

Allows users to enter their secure password.

Purpose:

Verifies user identity
Protects account access
Login Button

The login button submits the entered credentials for authentication.

Function:

Validates user input
Processes login request
Redirects successful users to the dashboard
Registration Link

Provides access to the registration page for new users.

Purpose:

Enables account creation
Improves accessibility for first-time users
Technologies Used

The login page was developed using frontend web technologies.

HTML

Used to create the structure and layout of the login page.

CSS

Used to style the page, including colors, fonts, spacing, and responsive design.

JavaScript

Used to perform client-side validation and enhance user interaction.

Form Validation

To improve data accuracy and user experience, form validation was implemented.

Validation Checks
Email Validation
Ensures the email field is not empty
Verifies correct email format
Password Validation
Ensures password field is not empty
Checks minimum password requirements
Error Messages
Displays meaningful messages for invalid inputs
Guides users to correct mistakes before submission

Validation helps prevent incorrect data entry and improves system reliability.

Responsive Design

The login page was designed to work effectively on various devices.

Supported Devices
Desktop Computers
Laptops
Tablets
Smartphones

Responsive design techniques ensure proper alignment and readability across different screen sizes.

User Experience Considerations

Several user experience principles were followed during development.

Simplicity

The interface contains only essential fields to avoid confusion.

Readability

Clear labels and appropriate font sizes improve readability.

Accessibility

The design supports easy navigation and interaction.

Consistency

The login page follows the same design theme as the rest of the application.

                                                       Registration Page Development
Overview

The Registration Page Development phase focused on creating a user-friendly interface that allows new users to register and create an account in the AI-Driven Public Health Chatbot for Disease Awareness system. This page serves as the first step for users who want to access the chatbot services, disease awareness resources, and other features provided by the application.

The registration page was designed to collect essential user information while maintaining simplicity, accessibility, and ease of use. The main objective was to provide a smooth onboarding process for users and ensure that the entered information is valid and properly formatted.

Purpose of the Registration Page

The registration page allows users to create a new account and become authorized members of the chatbot platform. It acts as a bridge between first-time visitors and registered users who can access the complete functionality of the system.

The registration process helps in:

Creating new user accounts
Collecting user information
Maintaining user records in the database
Providing secure access to chatbot services
Personalizing the user experience

By registering, users gain access to disease awareness information and can interact with the chatbot more effectively.

Design Objectives

The registration page was developed with the following objectives:

Create a simple and intuitive registration process
Collect accurate user information
Reduce user input errors through validation
Provide a responsive design for all devices
Maintain consistency with the application's healthcare theme

The interface was designed to be understandable for users of all technical skill levels.

User Interface Design

The registration page follows a structured and organized layout that guides users through the account creation process.

Main Components
Project Header

Displays the project title:

AI-Driven Public Health Chatbot for Disease Awareness

This helps users understand the purpose of the application and creates a professional appearance.

Full Name Field

This field allows users to enter their complete name.

Purpose:

Identifies the user within the system
Supports user account management
Improves personalization
Email Address Field

Users enter their valid email address during registration.

Purpose:

Acts as a unique identifier
Used for login authentication
Supports future communication and notifications
Mobile Number Field

Allows users to provide their contact number.

Purpose:

Stores contact information
Supports future account verification features
Improves user record management
Password Field

Users create a secure password for their account.

Purpose:

Protects user accounts
Ensures secure access to the system
Confirm Password Field

Users re-enter the password to confirm accuracy.

Purpose:

Prevents password typing mistakes
Ensures password consistency
Register Button

The Register button submits the entered information and creates a new user account.

Functions:

Validates user input
Processes registration request
Stores user information
Redirects users to login or dashboard page
Login Link

Provides navigation for users who already have an account.

Purpose:

Improves usability
Allows easy access to the login page
Technologies Used

The registration page was developed using the following technologies:

HTML

Used to create the structure and form elements of the registration page.

CSS

Used for styling, layout design, colors, spacing, and responsiveness.

JavaScript

Used for client-side validation and interactive form behavior.

                                                     Dashboard Development
Overview

The Dashboard Development phase focused on creating the main user interface that users access after successfully logging into the AI-Driven Public Health Chatbot for Disease Awareness system. The dashboard serves as the central hub of the application, providing users with quick access to chatbot services, disease awareness resources, health tips, and other important features.

The dashboard was designed to be simple, informative, and easy to navigate. It acts as the primary interaction point where users can explore different functionalities of the system and access healthcare-related information efficiently.

Purpose of the Dashboard

The main purpose of the dashboard is to provide users with a centralized platform where they can access all major modules of the application without difficulty.

The dashboard helps users:

Access the AI chatbot quickly
Navigate through different sections of the application
View health awareness information
Access disease-related content
Receive health tips and recommendations
Improve overall user experience

It acts as a bridge between the user and the various functionalities offered by the chatbot system.

Design Objectives

The dashboard was developed with the following objectives:

Provide a user-friendly interface
Enable quick navigation between modules
Display important information clearly
Improve accessibility for users of all ages
Maintain a professional healthcare-oriented appearance
Support responsive design for multiple devices

The overall design emphasizes simplicity and efficiency while ensuring that users can easily locate the features they need.

Dashboard Layout Design

The dashboard layout was carefully structured to ensure easy navigation and efficient information presentation.

Main Components
Header Section

The header section contains:

Project Logo
Project Title
User Profile Icon
Logout Option

The header provides branding and allows users to manage their session easily.

Welcome Section

A welcome section was added to greet users after login.

Example Message:

Welcome to the AI-Driven Public Health Chatbot for Disease Awareness. Explore health information and interact with the chatbot for disease awareness guidance.

This section helps create a positive user experience and introduces users to the platform.

Navigation Menu

The dashboard includes a navigation menu that allows users to move between different modules.

Navigation Options
Home
Chatbot
Disease Information
Health Tips
Contact
Logout

The menu was designed to be simple and easily accessible.

Chatbot Access Panel

The chatbot panel is the most important section of the dashboard.

Features
Quick access to chatbot services
Start Chat button
Easy interaction interface
Fast navigation to chatbot screen
Purpose

This section encourages users to begin interacting with the AI chatbot and obtain disease-related information instantly.

Disease Awareness Section

A dedicated section was created to display disease awareness information.

Information Provided
Disease Names
Symptoms
Causes
Prevention Methods
Treatment Guidance

The information is presented in an organized manner using cards and content blocks.

Benefits
Improves public health awareness
Provides educational healthcare content
Helps users understand diseases better
Health Tips Section

The dashboard includes a health tips area that provides useful recommendations for maintaining good health.

Topics Covered
Personal Hygiene
Healthy Eating Habits
Physical Exercise
Disease Prevention
Vaccination Awareness
Purpose

This section promotes preventive healthcare practices and encourages healthy lifestyles.

Quick Access Cards

To improve usability, quick-access cards were included in the dashboard.

Cards Included
Chat with AI

Provides direct access to the chatbot.

Disease Information

Redirects users to disease awareness resources.

Health Tips

Displays health-related recommendations.

Contact Support

Allows users to reach administrators if needed.

These cards improve navigation speed and overall user engagement.

Responsive Design

The dashboard was designed using responsive design principles to ensure compatibility across multiple devices.

Supported Devices
Desktop Computers
Laptops
Tablets
Smartphones

The layout automatically adjusts according to screen size, ensuring consistent usability and readability.

User Interface Design

A healthcare-oriented visual theme was selected for the dashboard.

Color Scheme
Blue – Represents trust and reliability
Green – Represents health and wellness
White – Provides clarity and readability
Design Features
Clean layout
Consistent typography
Proper spacing
Attractive content cards
User-friendly navigation

The visual design helps create a professional and welcoming healthcare platform.

Dashboard Functionalities

The dashboard supports several important functionalities.

User Management
Display user information
Manage user sessions
Support logout functionality
Navigation Control
Access all major modules
Simplify user workflow
Information Display
Show disease awareness content
Display health recommendations
Present chatbot access options
Testing and Validation

The dashboard underwent testing to ensure functionality and usability.

Testing Activities
Navigation testing
Responsive design testing
Layout verification
Link functionality checks
Content display validation

Testing helped identify and correct layout inconsistencies and navigation issues.

                                                     CRUD Form Development
Overview

The CRUD Form Development phase focused on creating forms that allow users and administrators to manage data efficiently within the AI-Driven Public Health Chatbot for Disease Awareness system. CRUD stands for Create, Read, Update, and Delete, which are the four basic operations used to manage information in a database.

In this project, CRUD functionality was primarily implemented for managing disease-related information, awareness content, health alerts, and user records. These operations ensure that the system database remains accurate, updated, and easy to maintain.

Purpose of CRUD Forms

The main purpose of CRUD forms is to provide a structured way to interact with the database. Through these forms, administrators can add new records, view existing information, modify outdated data, and remove unnecessary entries.

CRUD forms help in:

Managing disease information efficiently
Updating awareness content regularly
Maintaining accurate database records
Improving data accessibility
Supporting system administration

These forms play a crucial role in keeping the chatbot knowledge base current and reliable.

CRUD Operations

Create Operation

The Create operation allows administrators to add new records to the database.

Example

Adding a new disease record with details such as:

Disease Name
Symptoms
Causes
Prevention Methods
Treatment Information
Purpose
Expands the chatbot knowledge base
Keeps disease information updated
Supports awareness campaigns
Benefits
Easy addition of new healthcare content
Improved information availability
Better system scalability 

Read Operation

The Read operation allows users or administrators to view and retrieve stored information from the database.

Example

Viewing:

Disease details
Health awareness content
User records
Health alerts
Purpose
Access existing information quickly
Display disease-related content to users
Verify stored records
Benefits
Faster information retrieval
Improved user experience
Easy monitoring of database content

Update Operation

The Update operation allows administrators to modify existing records whenever information changes.

Example

Updating:

Symptoms of a disease
Prevention methods
Treatment guidelines
Awareness content
Purpose
Maintain data accuracy
Reflect latest healthcare information
Improve chatbot response quality
Benefits
Accurate disease awareness information
Better healthcare guidance
Reduced outdated content

Delete Operation

The Delete operation allows administrators to remove unnecessary or outdated records from the database.

Example

Deleting:

Duplicate disease entries
Incorrect awareness content
Expired health alerts
Purpose
Maintain database cleanliness
Remove redundant information
Improve database performance
Benefits
Better data organization
Reduced storage usage
Improved system efficiency
CRUD Form Design

The forms were designed with simplicity and usability in mind.

Form Fields Included
Disease Management Form
Disease ID
Disease Name
Category
Symptoms
Causes
Prevention Methods
Treatment Information
Awareness Content Form
Content ID
Title
Description
Content Type
Publish Date
Health Alert Form
Alert ID
Alert Message
Severity Level
Alert Date

The forms provide a structured way to enter and manage information.

User Interface Features

Several UI features were included to improve usability.

Input Fields

Allow users to enter required information.

Action Buttons
Add
View
Update
Delete
Reset
Validation Messages

Display appropriate error messages when invalid data is entered.

Search Functionality

Allows administrators to locate records quickly before updating or deleting them.

                                                   Table and Search Features Development
Overview

The Table and Search Features Development phase focused on implementing efficient data viewing and retrieval functionality within the AI-Driven Public Health Chatbot for Disease Awareness system. These features allow users and administrators to quickly access, organize, and search disease-related information stored in the database.

Tables were used to display structured data in a clear and organized format, while search functionality was implemented to help users find specific information without manually browsing through large amounts of data.

The objective of this phase was to improve data accessibility, user experience, and system efficiency.

Purpose of Table and Search Features

The main purpose of these features is to enable efficient management and retrieval of information stored in the system.

These features help users and administrators:

View disease information in an organized manner
Search for specific diseases quickly
Access awareness content efficiently
Manage records more effectively
Improve overall system usability

By implementing table and search functionality, the system becomes more interactive and user-friendly.

Table Feature Development

The table feature was developed to display information in rows and columns, making it easier to read and manage data.

Data Displayed in Tables

The tables can display various types of information, including:

Disease Information
Disease ID
Disease Name
Category
Symptoms
Causes
Prevention Methods
User Information
User ID
Name
Email
Registration Date
Health Alerts
Alert ID
Disease Name
Alert Message
Severity Level
Alert Date
Awareness Content
Content ID
Title
Content Type
Publish Date

The tabular format improves readability and allows quick access to stored records.

Table Design Features

Several features were incorporated into the table design.

Structured Layout

Information is displayed in clearly defined rows and columns.

Responsive Design

Tables adjust automatically based on screen size and device type.

Easy Navigation

Users can easily scroll through records and locate information.

Organized Presentation

Data is grouped logically to improve readability.

User-Friendly Interface

Simple layouts ensure ease of use for both technical and non-technical users.

Search Feature Development

The search feature allows users to locate information quickly by entering keywords into a search box.

Purpose

The search functionality reduces the time required to find specific information and improves overall user experience.

Instead of manually browsing through records, users can directly search for relevant content.

Search Functionality

The search feature supports searching based on:

Disease Name

Example:

Dengue
Malaria
Diabetes
COVID-19
Symptoms

Example:

Fever
Headache
Cough
Fatigue
Disease Category

Example:

Viral Diseases
Bacterial Diseases
Chronic Diseases
Awareness Content

Users can search educational materials using keywords or titles.

Search Process Workflow

The search functionality follows a simple workflow:

User enters a keyword in the search box.
The system receives the search request.
The database is queried for matching records.
Relevant results are retrieved.
Results are displayed in a table format.
Users can view detailed information.

This process provides quick and accurate retrieval of information.

                                                              Frontend Testing
Overview

The Frontend Testing phase focused on verifying the functionality, usability, responsiveness, and performance of the user interface developed for the AI-Driven Public Health Chatbot for Disease Awareness. The purpose of testing was to ensure that all frontend components work correctly and provide a smooth user experience across different devices and browsers.

Frontend testing was performed after the development of major UI components such as the Login Page, Registration Page, Dashboard, Navigation Menu, CRUD Forms, Tables, Search Features, and Chatbot Interface.

Purpose of Frontend Testing

The main objective of frontend testing was to identify and fix issues before integrating the frontend with the backend system.

Frontend testing helps in:

Verifying user interface functionality
Ensuring responsive design
Detecting and fixing UI errors
Improving user experience
Validating form inputs
Ensuring proper navigation between pages

Testing ensures that the application is reliable, user-friendly, and ready for deployment.

Components Tested

The following frontend modules were tested:

Login Page
Email field validation
Password field validation
Login button functionality
Navigation to dashboard
Registration Page
User input validation
Password confirmation verification
Form submission process
Navigation to login page
Dashboard
Dashboard loading
Navigation menu functionality
Content display verification
Responsive layout testing
Navigation Module
Menu link validation
Page redirection testing
User accessibility checks
CRUD Forms
Input field validation
Button functionality
Form reset operations
Data display verification
Table and Search Features
Table display testing
Search functionality verification
Search result accuracy
Data filtering validation
Chatbot Interface
Message input testing
Send button functionality
Response display testing
Chat interface usability
Types of Frontend Testing Performed
Functional Testing

Functional testing was conducted to ensure that every feature works according to the project requirements.

Tested Functionalities
Login process
Registration process
Navigation links
Search operations
Form submissions
Dashboard interactions

Result: All functionalities worked as expected.

User Interface Testing

UI testing was performed to verify the appearance and layout of the application.

Areas Tested
Button alignment
Text readability
Form layout
Color consistency
Spacing and margins
Visual appearance

Result: The interface maintained a clean and professional healthcare-themed design.

Form Validation Testing

Form validation testing ensured that users enter correct information before submission.

Validation Checks
Empty field validation
Email format validation
Password matching validation
Required field verification

Result: Validation messages displayed correctly and prevented invalid submissions.

Navigation Testing

Navigation testing ensured that all links and menus function properly.

Tested Navigation Paths
Home → Login
Login → Dashboard
Dashboard → Chatbot
Dashboard → Disease Information
Dashboard → Health Tips

Result: All navigation paths functioned correctly.

Responsive Testing

Responsive testing was performed to verify compatibility across multiple devices.

Devices Tested
Desktop Computers
Laptops
Tablets
Smartphones
Areas Verified
Layout adaptation
Content visibility
Menu responsiveness
Form usability

Result: The application displayed properly on different screen sizes.

Browser Compatibility Testing

Browser testing ensured consistent performance across popular web browsers.

Browsers Tested
Google Chrome
Microsoft Edge
Mozilla Firefox
Verification Areas
Page rendering
CSS styling
JavaScript functionality
Form behavior

Result: The application functioned consistently across supported browsers.

Testing Tools Used

The following tools were used during frontend testing:

Visual Studio Code

Used to develop and debug frontend components.

Live Server

Used for local testing and real-time page updates.

Google Chrome Developer Tools

Used for inspecting UI elements and identifying frontend issues.

Test Cases Executed
Test Case 1 – Login Validation

Input: Empty Email and Password

Expected Result: Error message displayed.

Actual Result: Validation message shown successfully.

Status: Passed

Test Case 2 – Registration Validation

Input: Password and Confirm Password mismatch.

Expected Result: Validation error displayed.

Actual Result: Error message displayed correctly.

Status: Passed

Test Case 3 – Search Functionality

Input: Search keyword "Dengue"

Expected Result: Related disease records displayed.

Actual Result: Matching records displayed successfully.

Status: Passed

Test Case 4 – Navigation Testing

Input: Click Dashboard Menu Links

Expected Result: Redirect to corresponding pages.

Actual Result: Navigation worked correctly.

Status: Passed

                                                    Spring Boot Project Setup
Overview

The Spring Boot Project Setup phase focused on establishing the backend development environment for the AI-Driven Public Health Chatbot for Disease Awareness. Spring Boot was selected as the backend framework because it simplifies application development, provides built-in configuration support, and enables the creation of scalable and maintainable web applications.

The primary objective of this phase was to configure the backend structure, establish project dependencies, create the application architecture, and prepare the system for handling user requests, database operations, and chatbot services.

Purpose of Spring Boot Setup

The Spring Boot setup serves as the foundation of the backend system and enables communication between the frontend interface and the database.

The backend is responsible for:

Processing user requests
Managing business logic
Handling user authentication
Connecting to the database
Managing chatbot responses
Providing REST API services

This setup ensures efficient system performance and smooth integration between all application components.

Why Spring Boot?

Spring Boot was chosen for this project due to its advantages in developing modern web applications.

Benefits of Spring Boot
Simplified project configuration
Faster application development
Built-in server support
Easy database integration
REST API development support
High scalability and maintainability
Strong community support

These features make Spring Boot an ideal choice for developing healthcare-related applications.

Development Environment Setup

The backend development environment was prepared using the following tools and technologies.

Java Development Kit (JDK)

Java was installed as the primary programming language required for Spring Boot development.

Version Used: JDK 17 (or compatible version)

Spring Boot Framework

Spring Boot was used to build and manage the backend application.

IDE (Integrated Development Environment)

The project was developed using:

Spring Tool Suite (STS) / Eclipse
Visual Studio Code (optional)
IntelliJ IDEA (optional)
Build Tool

Maven was used for dependency management and project build automation.

Project Creation

The Spring Boot project was created using Spring Initializr.

Project Configuration
Project Type: Maven Project
Language: Java
Spring Boot Version: Latest Stable Version
Group ID: com.healthchatbot
Artifact ID: public-health-chatbot
Package Name: com.healthchatbot

These settings established the basic structure of the backend application.

Dependencies Added

Several Spring Boot dependencies were included to support project functionality.

Spring Web

Used for creating REST APIs and handling HTTP requests.

Purpose:

Receive frontend requests
Send chatbot responses
Enable communication between frontend and backend
Spring Data JPA

Used for database operations and data management.

Purpose:

Simplify database access
Manage CRUD operations
Handle entity relationships
MySQL Driver / SQLite Driver

Used to connect the application to the database.

Purpose:

Store disease information
Store user records
Manage chatbot-related data
Spring Boot DevTools

Used during development to improve productivity.

Benefits:

Automatic application restart
Faster development workflow
Project Structure

A well-organized folder structure was created to improve maintainability.

Main Packages
Controller Package

Handles incoming API requests from the frontend.

Responsibilities:

Receive user queries
Process HTTP requests
Return responses
Service Package

Contains business logic implementation.

Responsibilities:

Process chatbot operations
Manage disease information
Perform system-related tasks
Repository Package

Handles database communication.

Responsibilities:

Perform CRUD operations
Access stored data
Manage database queries
Entity Package

Contains database model classes.

Examples:

User Entity
Disease Entity
Feedback Entity
Health Alert Entity
Configuration Package

Stores application configuration settings.

Responsibilities:

Database configuration
Security settings
Application properties
Database Configuration

Database connectivity was configured to enable communication between Spring Boot and the database.

Configuration Activities
Database URL setup
Username and password configuration
Entity mapping setup
Connection verification
Purpose
Store user information
Store disease data
Store chatbot responses
Manage feedback records
API Development Preparation

The backend was configured to support RESTful API development.

APIs Planned
User APIs
User Registration
User Login
Disease APIs
Add Disease
View Disease Information
Update Disease Details
Delete Disease Records
Chatbot APIs
Submit Query
Generate Response
Retrieve Chat History

These APIs enable communication between frontend and backend components.

                                               Database Connectivity
Overview

The Database Connectivity phase focused on establishing a secure and reliable connection between the Spring Boot backend application and the database used in the AI-Driven Public Health Chatbot for Disease Awareness project. Database connectivity is essential for storing, retrieving, updating, and managing information required by the chatbot system.

The database acts as the central repository for user information, disease records, chatbot responses, health awareness content, feedback, and system-related data. By connecting the backend to the database, the application can efficiently access and manage data whenever users interact with the chatbot.

Purpose of Database Connectivity

The primary purpose of database connectivity is to enable communication between the application and the database.

The connectivity layer allows the system to:

Store user registration details
Save disease-related information
Retrieve disease awareness content
Manage chatbot responses
Store user feedback
Perform CRUD operations
Maintain data consistency and reliability

Without database connectivity, the application would not be able to persist or access information required for chatbot functionality.

Database Used

For this project, a relational database such as MySQL or SQLite was used to store and manage application data.

Advantages
Structured data storage
Fast data retrieval
Easy integration with Spring Boot
Support for CRUD operations
Improved data security and consistency

The database serves as the backbone of the chatbot knowledge management system.

Database Configuration

The database connection was configured within the Spring Boot application.

Configuration Activities
Creating the database
Configuring database URL
Setting username and password
Establishing database connection
Verifying successful connectivity

These configurations enable seamless interaction between the application and the database.

Data Stored in the Database

Several types of information are maintained within the database.

User Information

Stores user-related details such as:

User ID
Name
Email Address
Mobile Number
Registration Date
Disease Information

Stores disease awareness content including:

Disease Name
Symptoms
Causes
Prevention Methods
Treatment Information
Health Queries

Stores user-submitted health questions.

Chat Responses

Stores responses generated by the chatbot.

Feedback Records

Stores ratings and comments provided by users.

Health Alerts

Stores disease-related notifications and awareness alerts.

Database Tables

The project database consists of multiple tables designed to organize information efficiently.

User Table

Maintains user account information.

Disease Table

Stores disease-related awareness information.

Health Query Table

Records user health-related questions.

Chat Response Table

Stores chatbot-generated responses.

Feedback Table

Maintains user feedback and ratings.

Health Alert Table

Stores public health alert information.

These tables are interconnected using relationships and foreign keys.

Spring Boot Integration

Spring Boot was integrated with the database using Spring Data JPA.

Benefits
Simplified database operations
Reduced coding complexity
Automatic query generation
Easy entity management

Spring Data JPA enables efficient interaction between Java objects and database tables.

CRUD Operations Using Database Connectivity

The established database connection supports CRUD functionality.

Create

Add new disease information, user records, or health alerts.

Read

Retrieve disease information and chatbot responses.

Update

Modify existing disease records and awareness content.

Delete

Remove outdated or incorrect records.

These operations help maintain accurate and updated information within the system.

Workflow of Database Connectivity

The database interaction follows a structured workflow:

User submits a request through the frontend.
Request is received by the Spring Boot backend.
Backend processes the request.
Database query is executed.
Requested data is retrieved or updated.
Response is sent back to the frontend.
User receives the result.

This workflow ensures smooth communication between all system components.

Testing Database Connectivity

Several tests were performed to verify proper database communication.

Testing Activities
Connection establishment testing
Data insertion testing
Data retrieval testing
Update operation testing
Delete operation testing
Error handling verification
Results
Successful database connection established
Data stored correctly
Records retrieved accurately
CRUD operations performed successfully

The testing confirmed that the database integration was functioning as expected.

                                                                  Entity and Repository Creation
Overview

The Entity and Repository Creation phase focused on developing the data model and database access layer for the AI-Driven Public Health Chatbot for Disease Awareness project. This phase plays a crucial role in connecting the Spring Boot application with the database and managing data efficiently.

Entities were created to represent database tables as Java classes, while repositories were developed to perform database operations such as storing, retrieving, updating, and deleting records. Together, they form the foundation of the application's data management system.

Purpose of Entity and Repository Creation

The main objective of this phase was to establish a structured mechanism for interacting with the database.

This implementation helps in:

Mapping database tables to Java classes
Managing application data efficiently
Simplifying database operations
Reducing coding complexity
Supporting CRUD functionality
Improving maintainability and scalability

By using Spring Data JPA, database interactions become easier and more efficient.

Entity Creation
What is an Entity?

An Entity is a Java class that represents a table in the database. Each entity contains attributes that correspond to the columns of a database table.

Entities act as a bridge between the application and the database.

Purpose of Entities
Represent database tables
Store application data
Enable object-relational mapping (ORM)
Simplify database interaction
User Entity

The User Entity was created to store user-related information.

Attributes
User_ID
Name
Email
Phone_Number
Age
Gender
Location
Registration_Date
Purpose
Manage registered users
Store user profiles
Support authentication and user management
Disease Entity

The Disease Entity stores disease awareness information used by the chatbot.

Attributes
Disease_ID
Disease_Name
Category
Symptoms
Causes
Prevention_Methods
Treatment_Information
Purpose
Maintain disease knowledge base
Provide health awareness information
Support chatbot responses
Health Query Entity

This entity stores health-related questions submitted by users.

Attributes
Query_ID
User_ID
Query_Text
Query_Date
Query_Status
Purpose
Record user interactions
Track health-related queries
Support chatbot analytics
Chat Response Entity

This entity stores responses generated by the chatbot.

Attributes
Response_ID
Query_ID
Bot_ID
Response_Text
Response_Time
Purpose
Maintain chatbot response records
Improve system monitoring
Support future enhancements
Feedback Entity

The Feedback Entity stores user feedback regarding chatbot responses.

Attributes
Feedback_ID
User_ID
Response_ID
Rating
Comments
Feedback_Date
Purpose
Collect user opinions
Improve chatbot quality
Measure user satisfaction
Health Alert Entity

This entity stores disease-related alerts and notifications.

Attributes
Alert_ID
Disease_ID
Alert_Message
Alert_Date
Severity_Level
Purpose
Support awareness campaigns
Notify users about disease risks
Improve public health communication

Repository Creation
What is a Repository?

A Repository is a Spring Data JPA interface used to communicate with the database. It provides built-in methods for performing CRUD operations without writing complex SQL queries.

Repositories simplify database management and improve application efficiency.

Purpose of Repositories

Repositories were created to:

Access database records
Perform CRUD operations
Execute queries efficiently
Reduce development effort
Improve code maintainability
User Repository

The User Repository manages user-related database operations.

Functions
Save user information
Retrieve user records
Update user details
Delete user accounts
Benefits
Simplified user management
Efficient authentication support
Disease Repository

The Disease Repository handles disease-related data.

Functions
Add disease information
Retrieve disease records
Update disease details
Delete outdated disease entries
Benefits
Maintains chatbot knowledge base
Supports disease awareness content
Health Query Repository

This repository manages user health queries.

Functions
Store user questions
Retrieve query history
Track chatbot interactions
Benefits
Supports user activity monitoring
Enables future analytics
Chat Response Repository

The Chat Response Repository stores chatbot-generated responses.

Functions
Save chatbot responses
Retrieve response history
Manage interaction records
Benefits
Supports chatbot performance monitoring
Maintains conversation history
Feedback Repository

The Feedback Repository manages user feedback records.

Functions
Store user ratings
Retrieve feedback data
Analyze user satisfaction
Benefits
Helps improve chatbot quality
Supports continuous system enhancement
Health Alert Repository

The Health Alert Repository manages disease alert information.

Functions
Store alerts
Retrieve alert records
Update alert information
Benefits
Supports awareness notifications
Enhances public health communication

Workflow of Entity and Repository Interaction

The interaction between entities and repositories follows a simple workflow:

User submits information through the frontend.
Backend receives the request.
Repository processes the request.
Entity maps the data to the database table.
Database operation is performed.
Results are returned to the application.
Response is displayed to the user.

This workflow ensures smooth and efficient data handling. 

                                                          REST API Development
Overview

The REST API Development phase focused on creating communication endpoints between the frontend and backend components of the AI-Driven Public Health Chatbot for Disease Awareness project. REST APIs (Representational State Transfer Application Programming Interfaces) enable data exchange between users, the chatbot system, and the database.

The primary objective of this phase was to develop secure, scalable, and efficient APIs that allow the frontend application to send requests and receive responses from the Spring Boot backend.

Purpose of REST API Development

The REST APIs act as a bridge between the frontend interface and backend services.

The APIs help in:

User registration and login
Retrieving disease information
Processing chatbot queries
Managing health awareness content
Storing user feedback
Performing CRUD operations
Communicating with the database

These APIs ensure smooth interaction between all system components.

What is a REST API?

A REST API is a web service that allows different applications to communicate using HTTP requests.

Common HTTP Methods
GET

Used to retrieve information from the server.

Example:

Get disease details
View user information
POST

Used to send data to the server.

Example:

Register a new user
Submit a chatbot query
PUT

Used to update existing records.

Example:

Update disease information
Modify user details
DELETE

Used to remove records.

Example:

Delete outdated disease records
Remove unnecessary alerts
User Management APIs
User Registration API

This API allows new users to create accounts.

Functions
Accept user details
Validate input data
Store information in the database
Generate successful registration response
Benefits
Secure account creation
Efficient user management
User Login API

This API authenticates registered users.

Functions
Verify email and password
Validate user credentials
Allow secure access to the system
Benefits
Secure authentication
Controlled system access
Disease Information APIs
View Disease Information API

This API retrieves disease-related information from the database.

Information Provided
Disease Name
Symptoms
Causes
Prevention Methods
Treatment Information
Benefits
Fast information retrieval
Supports chatbot responses
Add Disease API

Used by administrators to add new disease records.

Functions
Accept disease details
Store information in database
Update knowledge base
Benefits
Easy content management
Expands disease database
Update Disease API

Allows administrators to modify existing disease information.

Functions
Update symptoms
Update prevention methods
Update treatment information
Benefits
Maintains accurate health information
Improves chatbot response quality
Delete Disease API

Used to remove outdated or incorrect disease records.

Benefits
Maintains database accuracy
Improves system performance
Chatbot APIs
Submit Health Query API

This API receives health-related questions from users.

Example Queries
What are the symptoms of dengue?
How can malaria be prevented?
What causes diabetes?
Functions
Receive user input
Forward query for processing
Generate chatbot response
Benefits
Supports real-time chatbot interaction
Improves user engagement
Chat Response API

This API sends chatbot-generated responses back to users.

Functions
Retrieve disease information
Generate response
Return answer to frontend
Benefits
Provides instant health awareness information
Supports conversational interaction
Feedback APIs
Submit Feedback API

Allows users to provide ratings and comments regarding chatbot responses.

Information Collected
Rating
Feedback Comments
Response Reference
Benefits
Measures user satisfaction
Supports system improvement
View Feedback API

Used by administrators to review user feedback.

Benefits
Helps improve chatbot quality
Supports performance evaluation
Health Alert APIs
View Health Alerts API

Retrieves health alerts and disease awareness notifications.

Information Displayed
Disease Name
Alert Message
Severity Level
Alert Date
Benefits
Promotes public health awareness
Provides timely health information
API Architecture

The REST API architecture follows a layered approach.

Frontend Layer
Sends requests
Receives responses
Controller Layer
Handles API endpoints
Processes HTTP requests
Service Layer
Contains business logic
Processes application operations
Repository Layer
Communicates with database
Database Layer
Stores and manages data

This architecture improves scalability and maintainability.

API Workflow

The REST API workflow follows these steps:

User performs an action through the frontend.
Frontend sends an HTTP request.
Controller receives the request.
Service layer processes the request.
Repository accesses the database.
Data is retrieved or updated.
Response is generated.
Response is returned to the frontend.
User receives the result.

This workflow ensures efficient communication between all system components.

API Testing

After development, APIs were tested to verify functionality.

Testing Activities
Endpoint verification
Request validation
Response validation
Database connectivity testing
Error handling verification
Tools Used
Postman
Spring Boot Testing Tools
Browser Developer Tools
Results
APIs responded successfully
Database operations completed correctly
Error handling worked as expected

                                                        Authentication Module Development
Overview

The Authentication Module Development phase focused on implementing a secure user authentication mechanism for the AI-Driven Public Health Chatbot for Disease Awareness project. Authentication is an essential component that verifies the identity of users before granting access to the system and its features.

The authentication module ensures that only registered users can access the chatbot, disease awareness resources, dashboard, and other protected functionalities. It helps maintain system security, user privacy, and controlled access to application resources.

Purpose of Authentication Module

The primary purpose of the authentication module is to validate user identity and provide secure access to the application.

The module helps in:

User registration and account creation
User login and authentication
Protecting system resources
Preventing unauthorized access
Managing user sessions
Enhancing application security

By implementing authentication, the system ensures that users can safely interact with the chatbot and healthcare information services.

Importance of Authentication

In a healthcare-related application, user security and data protection are important considerations.

Authentication helps to:

Verify legitimate users
Protect sensitive information
Prevent unauthorized system usage
Improve user trust and reliability
Maintain secure access control

A secure authentication system improves the overall quality and reliability of the application.

User Registration Process
Overview

The registration process allows new users to create accounts and gain access to the chatbot platform.

Information Collected
Full Name
Email Address
Mobile Number
Password
Registration Workflow
User opens the registration page.
User enters required details.
System validates the entered information.
User information is stored in the database.
Registration confirmation is displayed.
User can proceed to the login page.
Benefits
Enables account creation
Supports user management
Provides personalized access
User Login Process
Overview

The login process verifies registered user credentials before granting access to the system.

Login Information
Email Address
Password
Login Workflow
User enters email and password.
System validates credentials.
Database verifies user information.
Authentication is successful.
User is redirected to the dashboard.
Benefits
Secure user access
Controlled system usage
Improved security
Authentication Components

Several components were developed to implement the authentication module.

Login Page

Provides the user interface for entering login credentials.

Features
Email field
Password field
Login button
Registration link
Purpose
Authenticate users
Provide access to protected resources
Registration Page

Allows new users to create accounts.

Features
User information form
Password confirmation
Registration button
Purpose
User onboarding
Account creation
Authentication Controller

The Authentication Controller handles login and registration requests.

Responsibilities
Receive user credentials
Validate requests
Process authentication
Return appropriate responses
Benefits
Centralized authentication handling
Improved application structure
Authentication Service

The Authentication Service contains the business logic related to user authentication.

Responsibilities
Validate credentials
Register users
Manage authentication processes
Benefits
Better code organization
Improved maintainability
User Repository

The User Repository communicates with the database during authentication.

Functions
Store user information
Retrieve user records
Verify login credentials
Benefits
Efficient database access
Simplified data management
Form Validation

Validation was implemented to ensure accurate user input.

Registration Validation
Checks Performed
Name field cannot be empty
Email format validation
Mobile number validation
Password strength verification
Password confirmation matching
Benefits
Prevents invalid registrations
Improves data quality
Login Validation
Checks Performed
Email field verification
Password field verification
Empty field validation
Benefits
Prevents authentication errors
Improves user experience
Session Management
Overview

Session management helps maintain the authenticated state of users after login.

Functions
Track active users
Maintain login sessions
Control user access
Benefits
Improved usability
Enhanced security
Database Integration

The authentication module was integrated with the database to store and verify user information.

Database Operations
User Registration
Store user records
Save authentication details
User Login
Retrieve user information
Verify credentials
Benefits
Reliable user management
Secure data storage
Security Features

Several security measures were considered during authentication module development.

Basic Security Measures
Password Protection

Passwords are used to secure user accounts.

Input Validation

All user inputs are validated before processing.

Controlled Access

Only authenticated users can access protected pages.

Error Handling

Appropriate error messages are displayed for invalid login attempts.

Future Security Enhancements

The following features can be added in future versions:

Password Encryption

Encrypt stored passwords using secure hashing algorithms.

JWT Authentication

Implement JSON Web Tokens for secure session management.

OTP Verification

Add one-time password verification during registration or login.

Role-Based Access Control

Provide different access levels for users and administrators.

Testing and Verification

The authentication module was thoroughly tested to ensure proper functionality.

Testing Activities
Registration Testing
New user registration
Validation testing
Duplicate account checks
Login Testing
Credential verification
Successful login testing
Invalid login testing
Database Testing
User record storage
Credential retrieval verification
Session Testing
Session creation
Session maintenance
Logout functionality 

                                                   Backend Business Logic Development
Overview

The Backend Business Logic Development phase focused on implementing the core functionality and decision-making processes of the AI-Driven Public Health Chatbot for Disease Awareness project. Business logic acts as the brain of the application, processing user requests, applying rules, interacting with the database, and generating appropriate responses.

This layer was developed using Spring Boot and serves as the bridge between the frontend user interface and the database. It ensures that all operations are performed correctly and that users receive accurate disease awareness information through the chatbot.

Purpose of Backend Business Logic

The main purpose of business logic is to handle application operations and enforce system rules.

The backend business logic is responsible for:

Processing user requests
Validating user inputs
Managing chatbot interactions
Retrieving disease information
Handling authentication processes
Managing database operations
Generating appropriate responses

This layer ensures that the application functions efficiently and consistently.

Importance of Business Logic

Business logic is a critical part of the application because it controls how data is processed and how the system behaves.

Benefits
Ensures accurate information delivery
Maintains data consistency
Reduces frontend complexity
Improves application security
Supports future scalability
Enhances maintainability

Without business logic, the system would not be able to process user requests effectively.

User Authentication Logic
Overview

Authentication logic was implemented to manage user registration and login processes.

Functions
Validate user credentials
Verify email and password
Create new user accounts
Prevent invalid login attempts
Workflow
User submits login credentials.
Backend validates input data.
User information is retrieved from the database.
Credentials are verified.
Access is granted if authentication is successful.
Benefits
Secure user access
Improved system security
Controlled access to resources
Disease Information Processing Logic
Overview

The disease management logic handles the storage, retrieval, and updating of disease-related information.

Functions
Add disease information
Retrieve disease details
Update disease records
Delete outdated records
Information Managed
Disease Name
Symptoms
Causes
Prevention Methods
Treatment Information
Benefits
Accurate disease awareness content
Efficient information management
Reliable chatbot knowledge base
Chatbot Query Processing Logic
Overview

The chatbot processing logic is the core functionality of the system.

It receives user health-related questions and generates appropriate responses.

Example Queries
What are the symptoms of dengue?
How can malaria be prevented?
What causes diabetes?
Processing Workflow
User submits a query.
Backend receives the request.
Query is analyzed.
Relevant disease information is searched.
Appropriate response is generated.
Response is sent to the user.
Benefits
Real-time information delivery
Improved user engagement
Faster access to health awareness content
Disease Awareness Recommendation Logic
Overview

This logic provides preventive healthcare recommendations and awareness tips.

Functions
Suggest preventive measures
Provide health awareness information
Recommend healthy habits
Encourage medical consultation when necessary
Examples
Wash hands regularly
Drink clean water
Follow vaccination schedules
Consult a healthcare professional for severe symptoms
Benefits
Promotes disease prevention
Supports public health awareness
Encourages healthy lifestyles
Feedback Management Logic
Overview

Feedback management logic collects and processes user feedback regarding chatbot responses.

Functions
Store user ratings
Save comments
Analyze satisfaction levels
Benefits
Improves chatbot quality
Supports future enhancements
Helps identify improvement areas
Health Alert Processing Logic
Overview

This logic manages disease-related alerts and awareness notifications.

Functions
Retrieve health alerts
Display awareness messages
Update alert information
Benefits
Provides timely health updates
Improves public awareness
Supports disease prevention efforts
CRUD Business Logic
Overview

CRUD logic handles Create, Read, Update, and Delete operations within the application.

Create

Add new disease records, awareness content, or user information.

Read

Retrieve stored information from the database.

Update

Modify existing records when information changes.

Delete

Remove outdated or unnecessary records.

Benefits
Efficient data management
Accurate database maintenance
Improved application reliability
Service Layer Implementation
Overview

The Service Layer contains the business logic implementation.

Responsibilities
Process requests from controllers
Perform validation
Execute business rules
Communicate with repositories
Advantages
Better code organization
Improved maintainability
Easier testing and debugging
Database Interaction Logic
Overview

Business logic communicates with repositories to access and manage database records.

Operations Performed
Save data
Retrieve records
Update information
Delete records
Benefits
Efficient database communication
Consistent data management
Reduced coding complexity
Error Handling Logic
Overview

Error handling mechanisms were implemented to manage unexpected situations.

Examples
Invalid login credentials
Missing user input
Disease record not found
Database connection failures
Benefits
Improved user experience
Better system stability
Easier troubleshooting
Workflow of Backend Business Logic

The complete workflow follows these steps:

User submits a request through the frontend.
Controller receives the request.
Service layer processes the request.
Business rules are applied.
Repository communicates with the database.
Data is retrieved or updated.
Response is generated.
Controller sends the response to the frontend.
User receives the result.

This workflow ensures smooth and efficient application operation.

                                                      API Testing Using Postman
Overview

The API Testing Using Postman phase focused on validating and verifying the functionality of the REST APIs developed for the AI-Driven Public Health Chatbot for Disease Awareness project. Postman was used as the primary testing tool to ensure that all API endpoints worked correctly, returned accurate responses, and successfully communicated with the database.

API testing plays a critical role in backend development because it helps identify issues before integrating the APIs with the frontend application. Through systematic testing, the reliability, performance, and correctness of the backend services were verified.

Purpose of API Testing

The primary objective of API testing was to ensure that all backend services function as expected.

API testing helps in:

Verifying API functionality
Validating request and response data
Testing database connectivity
Detecting errors and bugs
Ensuring proper communication between frontend and backend
Improving application reliability

Through API testing, the backend system becomes more stable and ready for deployment.

Why Postman?

Postman is a popular API testing and development platform that allows developers to send HTTP requests and analyze responses.

Advantages of Postman
Easy-to-use interface
Supports all HTTP methods
Fast API testing
Response visualization
Error debugging
Collection management
Automated testing support

These features make Postman an effective tool for testing Spring Boot REST APIs.

APIs Tested

Several APIs developed for the chatbot application were tested using Postman.

User Registration API
Purpose

To create new user accounts.

Request Data
Name
Email
Mobile Number
Password
Expected Result
User information stored successfully
Registration confirmation message returned
Outcome

The API successfully created user accounts and stored data in the database.

User Login API
Purpose

To authenticate registered users.

Request Data
Email
Password
Expected Result
Successful login for valid credentials
Error message for invalid credentials
Outcome

Authentication functionality worked correctly and validated user credentials successfully.

Disease Information API
Purpose

To retrieve disease-related information from the database.

Data Retrieved
Disease Name
Symptoms
Causes
Prevention Methods
Treatment Information
Expected Result

Disease details returned successfully.

Outcome

The API correctly fetched and displayed disease information.

Add Disease API
Purpose

To insert new disease records into the database.

Expected Result

New disease information stored successfully.

Outcome

Disease records were added successfully and became available for chatbot queries.

Update Disease API
Purpose

To modify existing disease information.

Expected Result

Updated disease details saved in the database.

Outcome

Records were updated successfully.

Delete Disease API
Purpose

To remove outdated disease records.

Expected Result

Selected disease record deleted successfully.

Outcome

Delete operation performed correctly.

Chatbot Query API
Purpose

To process user health-related questions.

Example Query

"What are the symptoms of dengue?"

Expected Result

Appropriate disease-related response generated.

Outcome

The API successfully processed user queries and returned relevant responses.

Feedback API
Purpose

To collect user feedback and ratings.

Expected Result

Feedback information stored in the database.

Outcome

Feedback records were saved successfully.

HTTP Methods Tested

The following HTTP methods were verified using Postman.

GET Request

Used to retrieve information.

Examples
Get disease details
View user information
Retrieve health alerts
Result

Data retrieved successfully.

POST Request

Used to submit data to the server.

Examples
User registration
User login
Chatbot query submission
Result

Data inserted successfully.

PUT Request

Used to update existing records.

Examples
Update disease information
Modify awareness content
Result

Records updated correctly.

DELETE Request

Used to remove records.

Examples
Delete disease records
Remove outdated alerts
Result

Records deleted successfully.

Testing Workflow

The API testing process followed a structured workflow.

Step 1

Launch Postman application.

Step 2

Select API endpoint URL.

Step 3

Choose appropriate HTTP method.

Step 4

Provide request data if required.

Step 5

Send request.

Step 6

Analyze response.

Step 7

Verify database changes.

Step 8

Document results.

This workflow ensured consistent and accurate testing.

Response Validation

API responses were verified based on:

Status Codes
200 OK
201 Created
400 Bad Request
401 Unauthorized
404 Not Found
500 Internal Server Error
Response Data
Accuracy of returned information
Correct JSON structure
Proper error messages

Response validation ensured that APIs behaved as expected.

Database Verification

After API execution, database records were verified.

Verification Activities
Data insertion validation
Record update verification
Delete operation confirmation
Query result verification
Outcome

Database operations were performed accurately and consistently.

Error Handling Testing

Several error scenarios were tested.

Examples
Invalid Login Credentials

Expected Result: Authentication error message.

Missing Required Fields

Expected Result: Validation error displayed.

Non-Existing Disease Record

Expected Result: Record not found message.

Outcome

Error handling worked correctly and provided meaningful feedback. 

                                                                  Frontend and Backend Integration
Overview

The Frontend and Backend Integration phase focused on connecting the user interface developed using HTML, CSS, and JavaScript with the backend services developed using Spring Boot for the AI-Driven Public Health Chatbot for Disease Awareness project. This integration enabled seamless communication between users, the chatbot application, and the database.

The primary objective of this phase was to ensure that user actions performed on the frontend are processed by the backend, and the results are returned and displayed correctly on the user interface.

Purpose of Frontend and Backend Integration

The main purpose of integration is to establish communication between the client-side interface and server-side application logic.

The integration helps in:

Connecting web pages to backend services
Sending user requests to the server
Retrieving information from the database
Displaying dynamic data on the frontend
Processing chatbot interactions
Managing user authentication
Supporting real-time application functionality

Without integration, the frontend and backend would function independently without exchanging information.

Technologies Used
Frontend Technologies
HTML
CSS
JavaScript
Backend Technologies
Spring Boot
Java
REST APIs
Database
MySQL / SQLite
Testing Tool
Postman

These technologies work together to create a complete web application.

Integration Architecture

The application follows a three-tier architecture.

Presentation Layer (Frontend)

Handles user interaction.

Components:

Login Page
Registration Page
Dashboard
Chatbot Interface
Disease Awareness Module
Business Logic Layer (Backend)

Processes requests and applies application logic.

Components:

Controllers
Services
Authentication Module
Chatbot Processing Module
Data Layer (Database)

Stores application information.

Components:

User Data
Disease Information
Chatbot Responses
Feedback Records
Health Alerts
Integration Workflow

The integration process follows a structured workflow.

Step 1

User performs an action on the frontend.

Examples:

Login
Registration
Disease Search
Chatbot Query Submission
Step 2

JavaScript sends an HTTP request to the Spring Boot REST API.

Step 3

The backend controller receives the request.

Step 4

Business logic processes the request.

Step 5

The backend interacts with the database if necessary.

Step 6

A response is generated.

Step 7

The response is returned as JSON data.

Step 8

The frontend receives the response and updates the user interface.

This workflow ensures smooth communication between all application components.

User Authentication Integration
Registration Integration

The registration page was connected to the backend registration API.

Process
User enters registration details.
Data is validated.
Request sent to backend.
User information stored in database.
Success message displayed.
Benefits
Automated account creation
Secure data storage
Login Integration

The login page was integrated with the authentication API.

Process
User enters login credentials.
Request sent to backend.
Credentials verified.
User redirected to dashboard.
Benefits
Secure authentication
Controlled access to application features
Dashboard Integration
Overview

The dashboard was integrated with backend services to display dynamic content.

Data Displayed
User information
Disease awareness content
Health tips
Health alerts
Benefits
Dynamic content loading
Improved user experience
Chatbot Integration
Overview

The chatbot interface was integrated with backend APIs to process user queries.

Workflow
User enters a health-related question.
Query sent to backend API.
Backend processes the request.
Disease information retrieved.
Response returned.
Chatbot displays answer.
Example

User: What are the symptoms of dengue?

System Response: Fever, headache, muscle pain, nausea, and skin rash.

Benefits
Real-time interaction
Instant disease awareness information
Disease Information Integration
Overview

The disease awareness module was connected to backend APIs.

Features
View disease information
Search diseases
Retrieve awareness content
Data Retrieved
Disease Name
Symptoms
Causes
Prevention Methods
Treatment Information
Benefits
Dynamic information retrieval
Improved healthcare awareness
CRUD Operations Integration
Overview

CRUD forms were integrated with backend services.

Create

Add new disease records.

Read

Retrieve disease information.

Update

Modify disease details.

Delete

Remove outdated records.

Benefits
Efficient data management
Real-time database updates
Search Feature Integration
Overview

The search functionality was connected to backend APIs.

Process
User enters search keyword.
Request sent to backend.
Database searched.
Matching records returned.
Results displayed.
Benefits
Fast information retrieval
Better user experience
JSON Data Exchange
Overview

Data exchange between frontend and backend was performed using JSON.

Advantages
Lightweight format
Easy to read
Fast data transfer
Widely supported
Example Data
User details
Disease information
Chatbot responses
Feedback records

JSON enables efficient communication between application layers.

                                                     Bug Fixing and Validation
Overview

The Bug Fixing and Validation phase focused on identifying, analyzing, and resolving issues encountered during the development of the AI-Driven Public Health Chatbot for Disease Awareness project. After integrating the frontend, backend, APIs, and database components, extensive testing was conducted to ensure that the system operated correctly and efficiently.

The primary objective of this phase was to improve application stability, enhance user experience, eliminate errors, and validate that all functionalities met the project requirements.

Purpose of Bug Fixing and Validation

The main purpose of this phase was to ensure that the application functions reliably under different usage scenarios.

This process helps in:

Identifying software defects
Correcting system errors
Improving application performance
Ensuring data accuracy
Validating user inputs
Enhancing system reliability
Preparing the project for deployment

Bug fixing and validation are essential for delivering a high-quality software application.

Bug Identification Process
Overview

Various testing techniques were used to identify issues within the system.

Areas Tested
Frontend Interface
Backend Services
REST APIs
Database Connectivity
User Authentication
Chatbot Functionality
Search Features
CRUD Operations

Any unexpected behavior observed during testing was documented and analyzed for resolution.

Frontend Bug Fixing
Overview

Frontend testing helped identify several user interface and usability issues.

Issues Identified
Form Validation Errors

Some input fields initially accepted incomplete or invalid data.

Solution

Additional validation rules were implemented to verify user inputs before submission.

Responsive Design Issues

Certain UI components were not displayed properly on smaller screens.

Solution

Responsive CSS styling and media queries were applied to improve mobile compatibility.

Navigation Problems

Some navigation links did not redirect users correctly.

Solution

Link mappings and routing configurations were corrected.

Outcome

Frontend pages became more stable, responsive, and user-friendly.

Backend Bug Fixing
Overview

Backend testing focused on validating business logic and API functionality.

Issues Identified
Request Processing Errors

Some API requests returned unexpected responses due to incomplete validation.

Solution

Improved request validation and exception handling mechanisms were implemented.

Service Layer Issues

Certain business logic operations produced inconsistent results.

Solution

Service methods were reviewed and corrected to ensure accurate processing.

Authentication Problems

Login validation occasionally failed due to incorrect credential handling.

Solution

Authentication logic was optimized and database queries were verified.

Outcome

Backend services became more reliable and produced accurate responses.

API Validation and Bug Fixing
Overview

REST APIs were tested extensively using Postman.

Issues Identified
Incorrect HTTP Responses

Some APIs returned incorrect status codes.

Solution

Response handling logic was updated to return proper HTTP status codes.

Missing Validation Checks

Certain APIs accepted invalid request data.

Solution

Additional input validation was implemented.

Endpoint Mapping Issues

A few API endpoints were incorrectly configured.

Solution

Controller mappings were reviewed and corrected.

Outcome

All API endpoints functioned correctly and produced expected results.

Database Validation and Fixing
Overview

Database operations were tested to ensure proper data storage and retrieval.

Issues Identified
Data Inconsistency

Some records were not updated correctly.

Solution

Repository methods and entity mappings were reviewed and corrected.

Foreign Key Relationship Errors

A few relationship mappings were initially incorrect.

Solution

Database schema and entity relationships were updated.

Duplicate Data Entries

Certain records could be inserted multiple times.

Solution

Additional validation checks were added before data insertion.

Outcome

Database operations became accurate and reliable.

Chatbot Validation
Overview

The chatbot functionality was tested using various disease-related queries.

Example Test Queries
What are the symptoms of dengue?
How can malaria be prevented?
What causes diabetes?
What are the symptoms of hypertension?
Validation Criteria
Response accuracy
Response speed
Information relevance
User understanding
Improvements Made
Refined response generation logic
Improved disease information retrieval
Enhanced response formatting
Outcome

The chatbot provided more accurate and consistent responses.

User Input Validation
Overview

Input validation was implemented across the application.

Registration Validation

Verified:

Name field
Email format
Mobile number format
Password matching
Login Validation

Verified:

Email input
Password input
Empty field checks
Search Validation

Verified:

Empty search keywords
Invalid search requests
Benefits
Reduced system errors
Improved data quality
Enhanced user experience
Error Handling Validation
Overview

Error handling mechanisms were tested to ensure graceful failure management.

Error Scenarios Tested
Invalid Login Credentials

Expected Result:

Appropriate error message displayed.

Disease Record Not Found

Expected Result:

User-friendly notification shown.

Database Connection Failure

Expected Result:

System displays controlled error response.

Invalid API Requests

Expected Result:

Validation message returned.

Outcome

The application handled errors effectively and prevented system crashes.

Performance Validation
Overview

Performance testing was conducted to evaluate application responsiveness.

Areas Evaluated
Page loading speed
API response time
Database query execution
Chatbot response generation
Results
Pages loaded efficiently
APIs responded quickly
Database operations executed successfully
Chatbot responses generated within acceptable time
Testing Tools Used

Several tools were used during validation.

Postman

Used for API testing and validation.

Google Chrome Developer Tools

Used for frontend debugging.

Spring Boot Logs

Used for backend error analysis.

Database Management Tools

Used to verify data storage and retrieval.
