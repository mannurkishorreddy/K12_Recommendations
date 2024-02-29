# Learning Equality Curriculum Recommendations: Streamlining K-12 Content Matching

## Overview
This competition focuses on developing a model to efficiently and accurately match K-12 educational content to specific curriculum topics. The challenge involves working with a diverse library of K-12 materials, organized into various topic taxonomies and spanning multiple languages, with a strong emphasis on STEM subjects. The aim is to facilitate easier access for students and educators to pertinent educational resources, enhancing the learning experience.

## Background
Globally, educational structures and objectives differ significantly. Most educational materials align with a single national system or lack a systematic organization, hindering easy discovery. Manually aligning digital materials to national curricula is time-consuming, resource-intensive, and requires expertise. This process is neither scalable nor sustainable in its current form, especially with the constant influx of new materials requiring realignment. There are no existing AI solutions to efficiently address these resource constraints in curriculum alignment.

Learning Equality, dedicated to the right to quality education, supports creating, adapting, and distributing open educational resources. They develop tools like Kolibri, designed for offline-first teaching and learning, especially for regions without internet access, which constitutes 37% of the global population. In collaboration with UNHCR, Learning Equality emphasizes the need for automated alignment tools to aid refugee learners and teachers with relevant digital learning resources. This initiative has involved curriculum designers, teachers, and machine learning experts and is now extended to participants in this competition.

## Competition Setup

### Environment Configuration
1. Set up AWS credentials:
   - Edit `~/.bash_profile` using `vim` and insert `export aws_UserName="yourName"`.
   - Run `os.environ['aws_UserName'] = {yourName}` in Python console.
   - Save `{yourName}_accessKeys.csv` on the desktop.
   - Execute `setEnvVariables.py`.

### Data Processing and Model Development
1. **Building Topic Trees**:
   - Utilize `pandas` for data handling.
   - For each channel, create a topic tree using `parent_id` and `child_id` relationships.
   - Merge parent and child nodes to construct a comprehensive topic tree for each level.

2. **Visualizing Curriculum Structure**:
   - Use `graphviz` to visualize topic trees, aiding in understanding the structure of specific curricula like CBSE.

3. **Modeling for Content Matching**:
   - Leverage models like `paraphrase-multilingual-mpnet-base-v2` and `all-miniLM-L6-v2` for semantic understanding.
   - Employ `NearestNeighbors` for finding relevant content.
   - Compute embeddings for content and topics, considering language variations.
   - Use a mean pooling strategy over embeddings to handle varied lengths of text.
   - Implement a customized F2 scoring system to evaluate model performance, focusing on precision and recall balance.

4. **Advanced Techniques and Final Submission**:
   - Explore sentence transformers for enhanced semantic matching.
   - Iterate over different model architectures to optimize content-topic alignment.
   - Submit the final predictions, ensuring compliance with competition guidelines.

### Additional Analysis
- Conduct a comprehensive analysis of the dataset, examining language distribution, content types, and correlation patterns among topics.
- Use data visualization tools like `seaborn` and `matplotlib` for insights into the dataset characteristics.
