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

