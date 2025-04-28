import openai
import config

client = openai.OpenAI(
    api_key=config.OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

def craft_resume(original_resume_text, job_description):
    prompt = f"Here is my original resume:\n{original_resume_text}\n\nPlease modify it to match this job description:\n{job_description}"
    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']


if __name__ == "__main__":
    original_resume_text = """
    Professional Resume for QE:

    Here’s a professional resume tailored for the **Automation Test Engineer (QA Engineer)** position, highlighting your skills and experiences at **Hypersonix.ai** and **Pratian Digital**:

    ---

    **Venkatesh Enakonda**  
    Kakinada, Andhra Pradesh | Venkateshenakonda7.ev@gmail.com | [LinkedIn](https://www.linkedin.com/in/venkatesh-enakonda-09ab591a5/) | +91 7075555313

    ---

    ### **Profile Summary**  
    Automation Test Engineer with over 1 year of experience managing automation projects and software testing throughout the testing lifecycle. Proven expertise in ensuring software performance and reliability through comprehensive quality assurance and automated testing processes. Skilled in implementing test plans, executing test cases, tracking bugs, and using advanced automation frameworks.

    ---

    ### **Professional Experience**

    **Quality Engineer**  
    *Pratian Digital, Bangalore, India*  
    *June 2022 – Present*

    - Conduct functional and UI testing of applications.
    - Create test plans with effort estimations, getting approvals from QA Lead and Team Lead.
    - Write detailed test scenarios and cases for sprint backlogs.
    - Identify and automate test cases for smoke testing scenarios.
    - Defect logging in Azure DevOps, maintaining requirements traceability.
    - Publish defect summaries and reports, categorizing issues by severity and priority.
    - Assess and communicate release risks to the Team Lead.
    - Prepare and present release notes for approval.
    - Participate in sprint initiation meetings, daily stand-ups, reviews, and retrospectives.

    **Key Achievements:**
    - Improved test case automation, reducing manual testing efforts.
    - Successfully delivered multiple sprint releases by adhering to tight timelines.

    ---

    **Data Engineer Intern**  
    *Hypersonix.ai, Bangalore, India*  
    *Dec 2021 – Mar 2022*

    - Developed APIs using FastAPI for customer onboarding processes.
    - Automated data parsing of complex XML files using Python, transforming the data for business operations.
    - Created REST APIs to generate user credentials, integrating with Snowflake and sending email confirmations.
    - Designed and implemented ETL pipelines utilizing Snowflake and AWS S3.
    - Written complex SQL queries to load, extract, and transform data in Snowflake and SQLite databases.

    **Technologies Used:** Python, SQL, FastAPI, Snowflake, Apache Airflow DAGs, AWS S3

    ---

    ### **Skills**

    - **Automation Frameworks:** Selenium, TestNG, JMeter, Jenkins, Cucumber  
    - **Programming Languages:** Core Java, Python  
    - **API Testing Tools:** Postman  
    - **Databases:** SQLite, MySQL, PostgreSQL  
    - **Bug Tracking Tools:** Azure DevOps  
    - **Others:** Database Testing, Performance Testing, ETL Pipelines, Version Control (Git)  
    - **Soft Skills:** Excellent Communication, Strong Requirements Understanding, Team Collaboration  

    ---

    ### **Projects**

    **JobCheck**  
    *Client: FirstMeridian*  
    *August 2022 – Present*

    Developed an automated solution for a job portal that connects job seekers and recruiters. The web application (Angular) and mobile apps (iOS and Android) enable users to apply for jobs and companies to find ideal candidates across various industries.  

    **Key Responsibilities:**  
    - Conduct functional, UI, and API testing.
    - Automated key workflows to ensure seamless jobseeker and recruiter interactions.

    ---

    ### **Education**

    **B.Tech in Mechanical Engineering**  
    Aditya College of Engineering and Technology, Andhra Pradesh, 2020

    ---

    ### **Certifications**  
    - Selenium Automation Tester  
    - API Testing with Postman
    """

    job_description = "Deep understanding and experience in Testing methodologies/approaches and test automation Experience in developing/working with different test automation frameworks Strong, hands-on experience in Java, RestAssured, Selenium, BDD (Cucumber) In-Depth understanding in testing APIs and experience in testing them manually (PostMan) and through automation Experience/Knowledge in working with variety of third party APIs Experience in using tools such as Maven, Git, BitBucket, Jira, Jenkins, Octane/ALM Knowledge/Experience to cloud tech (Kafka, S3) would be a plus Experience/Knowledge in payment & credit cards domain would be a plus Primary Skills: Java, RestAssured, Selenium, GIT, Jenkins, BDD, Jira API Testing (Postman), Testing Fundamentals Jenkins - One to Three Years, GIT - One to Three Years, Selenium - One to Three Years, Developer / Software Engineer One to Three Years, Java One to Three Years, Postman One to Three Years, JIRA - One to Three Years, REST Assured - One to Three Years, BDD - One to Three Years PSP Defined SCU in QET_AT_QA Automation Engineer"

    modified_resume = craft_resume(original_resume_text, job_description)
    print(modified_resume)
