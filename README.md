# Learning Equality Curriculum Recommendations
Enhance learning by matching K-12 content to target topics

The goal of this competition is to streamline the process of matching educational content to specific topics in a curriculum. You will develop an accurate and efficient model trained on a library of K-12 educational materials that have been organized into a variety of topic taxonomies. These materials are in diverse languages, and cover a wide range of topics, particularly in STEM (Science, Technology, Engineering, and Mathematics).

Your work will enable students and educators to more readily access relevant educational content to support and supplement learning.

# Context
Every country in the world has its own educational structure and learning objectives. Most materials are categorized against a single national system or are not organized in a way that facilitates discovery. The process of curriculum alignment, the organization of educational resources to fit standards, is challenging as it varies between country contexts.

Current efforts to align digital materials to national curricula are manual and require time, resources, and curricular expertise, and the process needs to be made more efficient in order to be scalable and sustainable. As new materials become available, they require additional efforts to be realigned, resulting in a never-ending process. There are no current algorithms or other AI interventions that address the resource constraints associated with improving the process of curriculum alignment.

Competition host Learning Equality is committed to enabling every person in the world to realize their right to a quality education, by supporting the creation, adaptation, and distribution of open educational resources, and creating supportive tools for innovative pedagogy. Their core product is Kolibri, an adaptable set of open solutions and tools specially designed to support offline-first teaching and learning for the 37% of the world without Internet access. Their close partner UNHCR has consistently highlighted the strong need and innovation required to create automated alignment tools to ensure refugee learners and teachers are provided with relevant digital learning resources. They have been jointly exploring this challenge in depth for the past few years, engaging with curriculum designers, teachers, and machine learning experts. In addition, Learning Equality is partnering with The Learning Agency Lab, an​ independent nonprofit focused on developing science of learning-based tools and programs for social good, along with UNHCR to engage you in this important process.

You have the opportunity to use your skills in machine learning to support educators and students around the world in accessing aligned learning materials that are relevant for their particular context. Better curriculum alignment processes are especially impactful during the onset of new emergencies or crises, where rapid support is needed, such as for refugee learners, and during school closures as took place during COVID-19.


# Setup - 

	1.	vim ~/.bash_profile
	2.	press i to go into insert mode
	3.	enter export aws_UserName="yourName"
	4.	press esc, then type :wq
	1.	Run os.environ['aws_UserName'] ={yourName} in your python console.
	2.	Save {yourName}_accessKeys.csv on your desktop.
	3.	Run setEnvVariables.py
