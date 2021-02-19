'''Hay Points

    William Ikenna-Nwosu (wiknwo)

    Each employee of a bureaucracy has a job description – 
    a few paragraphs that describe the responsibilities of 
    the job. The employee’s job description, combined with 
    other factors, such as seniority, is used to determine 
    his or her salary.

    The Hay Point system frees the Human Resources 
    department from having to make an intelligent judgement 
    as to the value of the employee; the job description is 
    merely scanned for words and phrases that indicate 
    responsibility. In particular, job descriptions that 
    indicate control over a large budget or management 
    over a large number of people yield high Hay Point 
    scores.

    You are to implement a simplified Hay Point system. 
    You will be given a Hay Point dictionary and a number 
    of job descriptions. For each job description you are 
    to compute the salary associated with the job, 
    according to the system
'''
def main():
    data = []

    # Get values for m and n
    data = input("").split(" ")
    data = list(map(int, data))
    m = data[0] # Number of words in haypoint dictionary
    n = data[1] # Number of descriptions
    data.clear()

    # Get words in haypoint dictionary
    haypoint_dict = {}
    for i in range(m):
        data = input("").split(" ")
        haypoint_dict[data[0]] = int(data[1])
    data.clear()
    
    # Get job descriptions
    job_descriptions = []
    job_description = ''
    for i in range(n):
        while not job_description.endswith('.'):
            line = input("")
            job_description = job_description + ' ' + line
            if job_description.endswith('.'):
                job_descriptions.append(job_description.rstrip('.'))
        job_description = ''
    
    # Compute haypoint value and salary based on job description
    haypointvalue = 0
    # for description in job_descriptions:
    #     for key in haypoint_dict.keys():
    #         if key in description:
    #             haypointvalue += haypoint_dict[key] * description.count(key)
    #     print(haypointvalue)
    #     haypointvalue = 0

    for i in range(len(job_descriptions)):
        job_descriptions[i] = job_descriptions[i].split(" ")
        for j in range(len(job_descriptions[i])):
            if job_descriptions[i][j] in haypoint_dict.keys():
                haypointvalue += haypoint_dict[job_descriptions[i][j]]
        print(haypointvalue)
        haypointvalue = 0

    
    
if __name__ == '__main__':
    main()