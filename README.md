# IBM-AI-Developer-Professional-course
This repository contains the labs and projects completed as part of the IBM AI Developer Professional course. The course covers a variety of topics, including web scraping, REST API development, data analysis, and machine learning, providing hands-on experience with key tools and technologies in AI development.

## Key Learning Areas
### 1. BeautifulSoup Fundamentals
- **Library Basics:**
  - Understanding BeautifulSoup's core functionality for HTML and XML parsing
  - Creating BeautifulSoup objects from HTML content
  - Working with HTML tree structures
- **HTML Navigation:**
  - Traversing HTML elements using parent-child relationships
  - Understanding and utilizing sibling relationships
  - Working with nested HTML structures

### 2. HTML Parsing Components
- **Tag Management:**
  - Working with HTML tags and their attributes
  - Accessing and manipulating tag content
  - Understanding tag hierarchies
- **String Handling:**
  - Working with NavigableString objects
  - Converting between NavigableString and Python strings
  - Extracting text content from HTML elements
 
### 3. Web Scraping Applications
- **Webpage Data Extraction:**
  - Downloading webpage content using requests
  - Extracting specific elements like links and images
  - Scraping data from HTML tables
- **Data Processing:**
  - Converting HTML tables to structured data
  - Using Pandas for table extraction (read_html)
  - Processing and formatting scraped data

 ### 4. Pandas Library in the context of an API
- **Data Operations:**
  - Converting dictionaries to DataFrames
  - Using DataFrame methods (head, mean)
  - Understanding Pandas with API communication flow

### 5. REST API Implementation
- **NBA API Usage:**
  - Making API requests using the NBA API
  - Working with team statistics and game data
  - Handling API endpoints and responses
- **Data Processing:**
  - Converting API responses to DataFrames
  - Filtering and analyzing game statistics
  - Calculating team performance metrics

### 6. Data Analysis and Visualization
- **Statistical Analysis:**
  - Computing means of game scores
  - Analyzing home vs. away game performance
  - Processing points and plus/minus statistics
- **Data Visualization:**
  - Creating plots using matplotlib
  - Visualizing game performance trends
  - Comparing home and away game statistics

### 7. Practical Skills
- **Data Handling:**
  - Working with JSON responses
  - Converting between different data formats
  - Filtering and subsetting data
- **API Integration:**
  - Making API calls
  - Handling API responses
  - Processing and analyzing API data

### 8. HTTP Protocol utilization
- **Client-Server Communication:**
  - Understanding how browsers send HTTP requests to servers
  - Learning how servers respond with desired resources
  - Grasping the basic flow of web communication
- **URL Structure:**
  - Breaking down URLs into scheme, base URL, and route
  - Understanding the difference between URLs and URIs
  - Learning about endpoints in web services

### 9. HTTP Methods and Status Codes
- **Request Methods:**
  - Deep dive into GET and POST methods
  - Understanding different HTTP methods and their purposes
  - Learning when to use each request type
- **Status Codes:**
  - Understanding response status codes (200, 404, etc.)
  - Learning the different status code classes
  - Interpreting server responses through status codes
- **File Operations:**
  - Downloading files through HTTP requests
  - Saving response content to files
  - Working with binary content like images
 
### 10. Mathematical Applications
- **Scientific Computing:**
  - Working with mathematical constants
  - Trigonometric functions
  - Creating evenly spaced sequences
  - Plotting mathematical functions

### 11. Matplotlib ractical Skills
- **Visualization:**
  - Basic plotting with matplotlib
  - Vector visualization
  - Creating linear sequences for plotting
  - Working with mathematical plots

### 12. RESTful API Development with Flask
- **Basic Flask Setup:**
  - Creating a Flask application instance
  - Implementing route handlers with decorators
  - Handling different HTTP methods (GET, POST, DELETE)
- **Request Handling:**
  - Processing query parameters using request.args
  - Handling URL parameters with route variables
  - JSON request body parsing with request.get_json()
  - UUID parameter handling with uuid converter

### 13. External API Integration
- **HTTP Client Usage:**
  - Making external API calls using the requests library
  - Handling different response status codes
  - URL encoding with urllib.parse.quote
 
### 14. API Design Patterns
- **Route Structure:**
  - Resource-based routing
  - Query parameter usage
  - URL parameter handling
  - HTTP method selection for different operations
- **Error Handling:**
  - Consistent error response format
  - HTTP status code usage
  - Global error handler implementation

### 15. Flask Practical Applications
- **Server-Client Communication:**
  - Understanding how Flask and JavaScript collaborate for web application functionality.
  - Handling both server-side and client-side operations for mathematical problem-solving.
- **Integration of Frontend and Backend:**
  - Bridging the gap between static HTML/JavaScript and dynamic Python code.

### 16. Python module creation and testing
- **Writing and structuring Python modules**
- **Implementing unit tests with unittest module**

### 17. Flask Web Framework for CRUD Operations
- **Flask Setup:**
  - Creating a Flask application instance.
  - Configuring routes and handling different HTTP methods (GET, POST).
  - Using render_template to render HTML templates and redirect for page redirection.
- **CRUD Operations:**
  - Implementing Create, Read, Update, and Delete operations in Flask.
  - Using form handling in HTML to capture user inputs and perform actions like creating, updating, and deleting records.
  - Implementing a simple in-memory database (using lists) for record management.
  - Handling URL parameters for dynamic content (e.g., updating or deleting a specific record by ID).
- **Template Rendering:**
  - Creating dynamic HTML pages (like create.html, read.html, update.html) to handle user interactions and display data.
  - Using Flask’s templating engine (Jinja) to pass data from the server to the front end.

### 18. Audio to Text Transcription using Whisper
- **Whisper Model Integration:**
  - Using the whisper library to load and interact with pre-trained models for automatic speech recognition (ASR).
  - Loading the "base" Whisper model and using it for transcribing audio files to text.
  - Handling various audio formats and performing transcription on audio files.

### 19. Machine Learning Integration
- **Watsonx API:**
  - Integrated IBM Watsonx for processing natural language tasks using a pre-trained model. Configured authentication with API keys and project IDs from IBM Cloud.
- **HuggingFace Embeddings:**
  - Used HuggingFace models (like sentence-transformers/all-MiniLM-L6-v2) for converting text data into embeddings to enable better semantic understanding and response generation.
 
### 20. Document Processing
- **File Upload:**
  - Enabled users to upload PDF documents, which are then processed for analysis and interaction.
- **Document Analysis:**
  - Extracted text from PDFs and enabled querying based on the document content.
 
### 21. Docker for Containerization
- **Dockerizing the Application:**
  - Used Docker to containerize the application, making it easier to deploy in any environment without worrying about dependency issues.

### 22. Speech-to-Text with Transformers
- Loading and using pre-trained models from Hugging Face
- Batch processing for speech-to-text conversion
- Handling audio input and output

### 23. Gradio for Interactive UIs
- Created user interfaces for speech-to-text applications
- Created web interface that allows users to upload audio files

### 24. IBM Watsonx LLM Integration
- **Speech-to-Text:**
  - Integrating IBM Watson’s Speech-to-Text API to transcribe spoken language into text.
  - Handling various language inputs and ensuring accurate transcription.
- **Text-to-Speech:**
  - Using IBM Watson’s Text-to-Speech API to convert generated text responses into audible speech.
  - Fine-tuning voice settings (pitch, speed, and tone) for a natural-sounding assistant.
- Setting up IBM Watsonx credentials and parameters for text generation
- Integrating Langchain with Watsonx for dynamic prompt processing
- Using LLMChain to connect the model with specific prompt templates

### 25. OpenAI API Integration
- **API Setup:**
  - Registering and configuring OpenAI API keys for integration with the voice assistant.
  - Implementing the OpenAI API to process natural language input and generate responses.
- **Natural Language Processing (NLP):**
  - Using GPT-3 or GPT-4 for processing complex user queries and generating human-like responses.
  - Configuring conversation contexts and handling multi-turn dialogues with OpenAI models.

### 26. Voice Command Recognition
- **Voice Command Handling:**
  - Implementing voice command recognition to trigger specific actions or queries.
  - Recognizing user intent and mapping it to the appropriate response or action (e.g., providing information, setting reminders, etc.).
- **Continuous Listening:**
  - Implementing a continuous listening mode for hands-free operation, where the assistant is always ready to process new commands.

### 27. Resume Polishing with AI
- **Core Functionality:**
  - Using IBM Watson's LLAMA-2 model to generate polished resume content
  - Understanding the role of NLP in enhancing resume clarity and relevance
  - Integrating user input (resume content, job title, etc.) for customized recommendations
- **User Input Customization:**
  - Collecting user specifications for polishing instructions
  - Adapting responses based on specific roles or job descriptions
  - Generating content that aligns with the targeted job position

### 28. Cover Letter Generation
- **Text Generation Process:**
  - Utilizing LLAMA-2 to generate a personalized cover letter
  - Customizing the cover letter with job-specific information (company name, job description, etc.)
  - Ensuring the cover letter reflects the user’s qualifications as outlined in their resume
- **Content Personalization:**
  - Tailoring cover letters to match the language and tone of the job description
  - Incorporating resume content without adding irrelevant details
  - Adjusting the writing style for a professional tone

### 29. Career Advice Generation
- **AI-Driven Career Insights:**
  - Leveraging LLAMA-2 to offer personalized career advice
  - Analyzing job descriptions and resumes to suggest improvements
  - Generating actionable tips to enhance resumes and match job requirements
- **Improvement Suggestions:**
  - Identifying key skills to highlight in resumes
  - Providing suggestions for resume formatting and content
  - Focusing on areas for improvement based on job descriptions
  
### 30. General Chatbot Functionality
- **General AI Conversations:**
  - Using LLAMA-2 for generating responses to various user queries
  - Understanding the versatility of LLAMA-2 in a conversational AI context
  - Engaging with users through text-based interaction for a wide range of topics
- **Natural Language Understanding:**
  - Recognizing different types of user queries
  - Generating coherent, contextually appropriate responses
  - Handling various question formats, from simple facts to complex discussions
