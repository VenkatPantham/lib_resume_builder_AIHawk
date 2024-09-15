from lib_resume_builder_AIHawk.template_base import *


prompt_header = """
Act as an HR expert and resume writer specializing in ATS-friendly resumes. Your task is to create a professional and polished header for the resume. The header should:

1. **Contact Information**: Include your full name, city and country, phone number, email address, LinkedIn profile, and GitHub profile.
2. **Formatting**: Ensure the contact details are presented clearly and are easy to read.

To implement this:
- If any of the contact information fields (e.g., LinkedIn profile, GitHub profile) are not provided (i.e., `None`), omit them from the header.

- **My information:**  
  {personal_information}
""" + prompt_header_template

prompt_education = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to articulate the educational background for a resume, ensuring it aligns with the provided job description. For each educational entry, ensure you include:

1. **Institution Name and Location**: Specify the university or educational institution’s name and location.
2. **Degree and Field of Study**: Clearly indicate the degree earned and the field of study.

To implement this, follow these steps:
- If the exam details are not provided (i.e., `None`), skip the coursework section when filling out the template.
- If the exam details are available, fill out the coursework section accordingly.


- **My information:**  
  {education_details}

- **Job Description:**  
  {job_description}
"""+ prompt_education_template


prompt_working_experience = """
Act as an HR expert and resume writer specializing in creating ATS-friendly resumes. Your task is to detail the work experience for a resume, ensuring it aligns precisely with the provided job description. For each job entry, include the following:

1. **Company Name and Location**: Clearly state the name of the company and its geographical location.
2. **Job Title**: Accurately state your job title, ensuring it matches or closely aligns with titles used in the job description.
3. **Dates of Employment**: Provide the start and end dates in the format (Month Year – Month Year).
4. **Responsibilities and Achievements**:
   - **Responsibilities**: List key responsibilities using bullet points.
   - **Achievements**: Highlight notable achievements with measurable results.

**Ordering:**
- Order the work experiences by the latest dates first (most recent at the top), and proceed chronologically

**Formatting Guidelines:**
- Use **bullet points** for clarity and readability.
- Begin each bullet point with a **strong action verb** (e.g., Developed, Implemented, Led).
- **Quantify achievements** where possible (e.g., "Increased sales by 20%").
- **Align terminology** with the job description to ensure keyword matching.
- Use **standard fonts** (e.g., Arial, Calibri, Times New Roman) and avoid special characters or symbols.
- Maintain **consistent formatting** (e.g., font size, bullet style) throughout the section.

**Keyword Optimization:**
- **Extract and integrate exact keywords** and phrases from the job description.
- Use **both singular and plural forms** of keywords where applicable.
- Include **synonyms and related terms** to cover various ways candidates might describe the same skill or experience.

**Implementation Instructions:**
- If any details (e.g., responsibilities, achievements) are not provided (i.e., `None`), **omit those sections** when filling out the template.
- Ensure **consistency in formatting and terminology** across all entries to improve ATS parsing.
- **Avoid using images, graphics, or tables** that ATS cannot parse.

- **My information:**  
  {experience_details}

- **Job Description:**  
  {job_description}
""" + prompt_working_experience_template

prompt_side_projects = """
Act as an HR expert and resume writer specializing in creating ATS-friendly resumes. Your task is to highlight notable side projects, ensuring they align with the provided job description. For each project, include the following:

1. **Project Name and Link**: Provide the name of the project and include a hyperlink to the GitHub repository or project page.
2. **Project Details**: Describe any notable recognition or achievements related to the project, such as GitHub stars, community feedback, or media mentions.
3. **Technical Contributions**: Highlight your specific contributions and the technologies used. Ensure the technologies align with those mentioned in the job description.

**Formatting Guidelines:**
- Use **bullet points** for clarity.
- Start each bullet with a **strong action verb** (e.g., Developed, Designed, Engineered).
- **Incorporate relevant keywords** and phrases from the job description.
- Use **standard fonts** (e.g., Arial, Calibri, Times New Roman) and avoid special characters or symbols.
- Maintain **consistent formatting** (e.g., font size, bullet style) throughout the section.

**Keyword Optimization:**
- **Include exact keywords** from the job description related to technologies and skills.
- Use **both full forms and acronyms** of relevant terms (e.g., "Machine Learning (ML)").

**Implementation Instructions:**
- If any details (e.g., link, achievements) are not provided (i.e., `None`), **omit those sections** when filling out the template.
- Ensure the project descriptions **demonstrate relevant skills and achievements** aligned with the job description.
- **Avoid using non-text elements** that ATS cannot parse.

- **My information:**  
  {projects}

- **Job Description:**  
  {job_description}
""" + prompt_side_projects_template

prompt_achievements = """
Act as an HR expert and resume writer specializing in creating ATS-friendly resumes. Your task is to list significant achievements, ensuring they align with the provided job description. For each achievement, include the following:

1. **Award or Recognition**: Clearly state the name of the award, recognition, scholarship, or honor.
2. **Description**: Provide a brief description of the achievement and its relevance to your career or academic journey.

**Formatting Guidelines:**
- Use **bullet points** for each achievement.
- Start each bullet with the **award or recognition name**, followed by a description.
- Ensure descriptions are **concise and impactful**.
- Use **standard fonts** (e.g., Arial, Calibri, Times New Roman) and avoid special characters or symbols.
- Maintain **consistent formatting** (e.g., font size, bullet style) throughout the section.

**Keyword Optimization:**
- **Integrate exact keywords** and phrases from the job description within the achievement descriptions.
- Highlight how each achievement **aligns with the job requirements**.
- Use **both full forms and acronyms** of relevant terms if applicable.

**Implementation Instructions:**
- If any details (e.g., certifications, descriptions) are not provided (i.e., `None`), **omit those sections** when filling out the template.
- Ensure that the achievements **clearly highlight your accomplishments** and align with the job description.
- **Avoid using images, graphics, or tables** that ATS cannot parse.

- **My information:**  
  {achievements}

- **Job Description:**  
  {job_description}
""" + prompt_achievements_template

prompt_certifications = """
Act as an HR expert and resume writer specializing in creating ATS-friendly resumes. Your task is to list significant certifications, ensuring they align with the provided job description. For each certification, include the following:

1. **Certification Name**: Clearly state the full name of the certification.
2. **Description**: Provide a brief description of the certification and its relevance to your professional or academic career.

**Formatting Guidelines:**
- Use **bullet points** for each certification.
- Include both the **full name and the commonly used acronym** (if applicable).
- Ensure descriptions are **concise and relevant**.
- Use **standard fonts** (e.g., Arial, Calibri, Times New Roman) and avoid special characters or symbols.
- Maintain **consistent formatting** (e.g., font size, bullet style) throughout the section.

**Keyword Optimization:**
- **Integrate exact keywords** and phrases from the job description within the certification descriptions.
- Highlight how each certification **aligns with the job requirements**.
- Use **both full forms and acronyms** of relevant terms if applicable.

**Implementation Instructions:**
- If any details (e.g., descriptions) are not provided (i.e., `None`), **omit those sections** when filling out the template.
- Ensure that the certifications listed are **relevant to the job description** and **highlight your qualifications** effectively.
- **Avoid using images, graphics, or tables** that ATS cannot parse.

- **My information:**  
  {certifications}

- **Job Description:**  
  {job_description}
""" + prompt_certifications_template

prompt_additional_skills = """
Act as an HR expert and resume writer specializing in creating ATS-friendly resumes. Your task is to list additional skills relevant to the job. For each skill, include the following:

1. **Skill Category**: Clearly state the category or type of skill (e.g., Programming Languages, Tools, Soft Skills).
2. **Specific Skills**: List the specific skills or technologies within each category.
3. **Proficiency and Experience**: Briefly describe your experience and proficiency level with each skill, using quantifiable metrics where possible.

**Formatting Guidelines:**
- Organize skills into **clear categories** for better readability.
- Use **bullet points** under each category.
- Keep bullet points **short and concise**.
- Start each bullet with the **skill name**, followed by a brief description.
- Ensure **consistent formatting** across all skill categories.
- Use **standard fonts** (e.g., Arial, Calibri, Times New Roman) and avoid special characters or symbols.
- Maintain **consistent formatting** (e.g., font size, bullet style) throughout the section.

**Keyword Optimization:**
- **Integrate exact keywords** and phrases from the job description within the skills descriptions.
- Highlight **proficiency levels** using standard terms (e.g., "Advanced," "Intermediate," "Beginner").
- Use **both full forms and acronyms** of relevant terms if applicable.

**Implementation Instructions:**
- **Do not add any information** beyond what is listed in the provided data fields. Only use the information provided in the 'languages', 'interests', and 'skills' fields to formulate your responses.
- **Omit sections** if any of the skill details (e.g., languages, interests, skills) are not provided (i.e., `None`).
- Ensure that the skills listed **accurately reflect your expertise** and **align with the job requirements**.
- **Avoid using images, graphics, or tables** that ATS cannot parse.

- **My information:**  
  {languages}  
  {interests}  
  {skills}

- **Job Description:**  
  {job_description}
""" + prompt_additional_skills_template

summarize_prompt_template = """
As a seasoned HR expert, your task is to identify and outline the key skills and requirements necessary for the position of this job. Use the provided job description as input to extract all relevant information. This will involve conducting a thorough analysis of the job's responsibilities and the industry standards. You should consider both the technical and soft skills needed to excel in this role. Additionally, specify any educational qualifications, certifications, or experiences that are essential. Your analysis should also reflect on the evolving nature of this role, considering future trends and how they might affect the required competencies.

Rules:
- Remove boilerplate text.
- Include only relevant information to match the job description against the resume.
- Ensure all extracted keywords are included in their various forms (singular/plural, acronyms/full forms).

# Analysis Requirements
Your analysis should include the following sections:

1. **Job Title**
   - **Exact Title:** Ensure the job title matches industry standards and includes common variations.
   - **Alternative Titles:** List synonyms and related titles that candidates might use (e.g., "Software Engineer" vs. "Software Developer").

2. **Technical Skills**
   - **Programming Languages:** List specific languages required (e.g., Python, Java, C++).
   - **Software & Tools:** Identify essential software and tools (e.g., Salesforce, Adobe Creative Suite, AWS).
   - **Technical Certifications:** Specify necessary certifications (e.g., AWS Certified Solutions Architect, CCNA).
   - **Methodologies:** Include relevant methodologies (e.g., Agile, Scrum, Six Sigma).
   - **Other Relevant Technologies:** Mention additional technologies pertinent to the role (e.g., Machine Learning, Data Analysis, UX/UI Design).

3. **Soft Skills**
   - **Communication:** Verbal and written communication proficiency.
   - **Problem-Solving:** Analytical thinking and troubleshooting abilities.
   - **Time Management:** Ability to prioritize and manage multiple tasks.
   - **Teamwork:** Collaboration and interpersonal skills.
   - **Adaptability:** Flexibility in dynamic environments.

4. **Educational Qualifications and Certifications**
   - **Degree Level:** Specify required degrees (e.g., Bachelor’s Degree, Master’s Degree, Ph.D.).
   - **Field of Study:** Relevant disciplines related to the position (e.g., Computer Science, Business Administration).
   - **Preferred Certifications:** List industry-recognized certifications that enhance qualifications (e.g., PMP, CISSP).

5. **Professional Experience**
   - **Years of Experience:** Specify the required amount of experience (e.g., 5+ years in software development).
   - **Relevant Industries:** Identify specific sectors of experience (e.g., FinTech, Healthcare, E-commerce).
   - **Role-Specific Experience:** Detail experience related to the role's responsibilities (e.g., full-stack development, project management).
   - **Preferred Experience:** Highlight advanced roles or specialized projects (e.g., leadership positions, international projects).

6. **Role Evolution**
   - **Emerging Skills:** Identify skills that are becoming increasingly important due to technological advancements (e.g., AI integration, blockchain technology).
   - **Industry Trends:** Consider trends that may influence the role (e.g., remote work proficiency, sustainability practices).
   - **Anticipated Skill Development:** Emphasize the need for continuous learning and cross-functional expertise.

7. **Additional Keywords and Phrases**
   - **Action Verbs:** Include dynamic verbs relevant to the role (e.g., Developed, Implemented, Led).
   - **Qualifications Phrases:** Phrases that highlight qualifications (e.g., "Bachelor’s degree in," "Proven track record in").
   - **Industry-Specific Terms:** Niche terminology relevant to the role (e.g., "DevOps practices," "User Experience (UX) design").

# Final Result:
Your analysis should be structured in a clear and organized document with distinct sections for each of the points listed above. Each section should contain relevant keywords and phrases extracted from the job description, optimized for ATS matching.

# Job Description:
```
{text}
```

---

# Job Description Summary"""
