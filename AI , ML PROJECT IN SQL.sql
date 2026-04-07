create database AI_JOB ;
use AI_job;
CREATE TABLE aiml_jobs (
    job_id INT PRIMARY KEY,

    job_title VARCHAR(100) NOT NULL,
    company_size VARCHAR(50) NOT NULL,
    company_industry VARCHAR(100) NOT NULL,
    country VARCHAR(50) NOT NULL,

    remote_type VARCHAR(20) NOT NULL 
        CHECK (remote_type IN ('Remote', 'Hybrid', 'Onsite')),

    experience_level VARCHAR(20) NOT NULL 
        CHECK (experience_level IN ('Entry', 'Mid', 'Senior')),

    years_experience INT 
        CHECK (years_experience >= 0),

    education_level VARCHAR(50) NOT NULL,

    skills_python TINYINT(1) DEFAULT 0,
    skills_sql TINYINT(1) DEFAULT 0,s
    skills_sql TINYINT(1) DEFAULT 0,
    skills_ml TINYINT(1) DEFAULT 0,
    skills_deep_learning TINYINT(1) DEFAULT 0,
    skills_cloud TINYINT(1) DEFAULT 0,

    salary INT 
        CHECK (salary > 0),

    job_posting_month INT 
        CHECK (job_posting_month BETWEEN 1 AND 12),
    job_posting_year INT NOT NULL,

    hiring_urgency VARCHAR(20) 
        CHECK (hiring_urgency IN ('Low', 'Medium', 'High')),

    job_openings INT 
        CHECK (job_openings >= 0)
);
SELECT * FROM ai_Jobs;

-- 1 = Which country offers the highest salary?-- 

select country,max(salary) as highest_salary 
From  ai_jobs
group by country;


-- 2 = Which job title has the highest average salary?--
SELECT 
    job_title, AVG(salary) AS avg_salary
FROM
    ai_jobs
GROUP BY job_title
ORDER BY avg_salary DESC
LIMIT 1;

-- 3 = Which country has the most job postings in the dataset?-- 
SELECT country, COUNT(*) AS job_count
FROM ai_jobs
GROUP BY country
ORDER BY job_count DESC
LIMIT 3;

-- 4 = What is the average salary by experience level? 
SELECT experience_level, AVG(salary) AS avg_salary
FROM AI_Job
GROUP BY experience_level;

select experience_level , AVG(salary) as avg_salary 
from ai_jobs
group by experience_level;


-- 5 = What is the distribution of job postings by company size-- 

SELECT company_size, COUNT(*) AS job_count
FROM ai_Jobs
GROUP BY company_size;

----------------------------------------------- FILTTER  ------------------------------------------------------------------------------------------ 
-- "Which jobs have a salary greater than 150,000 and are located in Germany?"-- 
SELECT *
FROM ai_jobs
WHERE salary > 150000
  AND country =  'Germany';
  
  
  ---------------------------------------------------------------- JOIN ---------------------------------------------------------------------------------------
  
  SELECT 
    aj.job_title, 
    aj.salary, 
    aj.company_size, 
    aj.country, 
    aj.remote_type
FROM ai_jobs aj;


-- 6 = Which country has the most job postings?

SELECT country, COUNT(*) AS job_count
FROM ai_jobs
GROUP BY country
ORDER BY job_count DESC;

-- 7 = What is the average salary by experience level?

SELECT experience_level, AVG(salary) AS avg_salary
FROM ai_jobs
GROUP BY experience_level;


-- 8 = Which job title has the highest average salary?-- 
SELECT job_title, AVG(salary) AS avg_salary
FROM ai_jobs
GROUP BY job_title
ORDER BY avg_salary DESC
LIMIT 5;



  -- 9 What is the salary distribution by company size?
  
  SELECT company_size, COUNT(*) AS job_count
FROM ai_jobs
GROUP BY company_size;
  
   -- 10 What is the average salary by education level?-- 
   SELECT education_level, AVG(salary) AS avg_salary
FROM ai_jobs
GROUP BY education_level;


-- 11 = Which country offers the highest salary on average?
SELECT country, AVG(salary) AS avg_salary
FROM ai_jobs
GROUP BY country
ORDER BY avg_salary DESC
LIMIT 5;

-- 12 = How does salary vary by remote type (Remote, Hybrid, Onsite)?
SELECT remote_type, AVG(salary) AS avg_salary
FROM ai_jobs
GROUP BY remote_type;

-- 13 = What is the number of job openings by hiring urgency? 
SELECT hiring_urgency, SUM(job_openings) AS total_openings
FROM ai_jobs
GROUP BY hiring_urgency;

-- 14 Which skills are most commonly required? 

SELECT 'Python' AS skill, SUM(skills_python) AS count
FROM ai_jobs
UNION
SELECT 'SQL' AS skill, SUM(skills_sql) AS count
FROM ai_jobs
UNION
SELECT 'ML' AS skill, SUM(skills_ml) AS count
FROM ai_jobs
UNION
SELECT 'Deep Learning' AS skill, SUM(skills_deep_learning) AS count
FROM ai_jobs
UNION
SELECT 'Cloud' AS skill, SUM(skills_cloud) AS count
FROM ai_jobs
ORDER BY count DESC;
  
  
  
  
  
  
  
  
  
  