# AI-Reviewer-An-AI-tool-to-perform-Systematic-Literature-Reviewes

Full source code at: https://drive.google.com/file/d/1bF83IhYM9-LV0vkdStr5LF6l1DctLwiI/view?usp=sharing

![image](https://github.com/user-attachments/assets/339ceb6d-25f6-4ccb-a9bd-2e592363c0af)


![image](https://github.com/user-attachments/assets/2ddd56b8-c3d0-402d-b12f-a64710c0dbe7)


![image](https://github.com/user-attachments/assets/defd6fe8-6c82-471b-b69a-29201bffefa2)

![image](https://github.com/user-attachments/assets/5f4261da-5e29-447b-a471-789e73d4c33c)


![image](https://github.com/user-attachments/assets/801ebc1d-5ed1-403e-bd76-fccdd59facfc)



![image](https://github.com/user-attachments/assets/2b982771-4834-4d18-95a2-922a2be0659b)






![image](https://github.com/user-attachments/assets/d789c2df-495f-45fd-8bcb-dc9a7058c12d)

![image](https://github.com/user-attachments/assets/04cb3060-5707-4ca6-a523-22bd5e042764)


![image](https://github.com/user-attachments/assets/8fa4d6d0-048c-4e02-8631-f10fc5db8ecb)



![image](https://github.com/user-attachments/assets/a38ef939-335a-4e2c-ac89-3b17e3fce28e)


![image](https://github.com/user-attachments/assets/960ba58c-cdd8-489e-91ed-55fd7c516dfc)

![image](https://github.com/user-attachments/assets/3c86896a-bd6b-458a-a1e9-d310e55b93b4)


![image](https://github.com/user-attachments/assets/f5f08b82-99cc-4830-bb12-634bee555190)


![image](https://github.com/user-attachments/assets/9efe292b-49ff-4c14-afde-8cb6cbe74fbe)




file:///C:/Users/kucaa/Downloads/AIReviewer/index.html#intro

AI-Assisted Systematic Review: Web-Based and Automated Deep Learning for COVID-19 Detection in X-rays and CT Scans and Pneumonia Diagnosis in X-rays

Carlos Antunes1, João M F Rodrigues2  and António Cunha1,3

1Universidade de Trás-os-Montes e Alto Douro, Vila Real, Portugal
2NOVA LINCS & ISE, Universidade do Algarve, Faro, Portugal
 3ALGORITMI Research Centre, University of Minho, Guimarães, Portugal

Summary: COVID-19 and pneumonia require accurate and rapid diagnosis, yet traditional chest X-ray interpretation is limited by delays, inter-observer variability, and resource constraints. This systematic literature review (SLR) investigates the role of artificial intelligence (AI) and deep learning (DL) in web-based diagnostics, emphasizing explainable AI (XAI) for improved interpretability. To enhance the review process, a custom AI tool was developed to assist in literature analysis. A rigorous selection methodology, incorporating two filtering stages, screened 5,613 studies, narrowing them to 129 high-quality publications. The findings highlight significant advancements in AI-driven diagnostics, with deep learning models achieving superior precision, recall, and ROC metrics compared to conventional approaches. However, challenges such as model generalizability, inconsistent imaging protocols, and dataset standardization persist.
To address these limitations, this study presents an AI-powered diagnostic framework integrating large language models (LLMs), visual-language models (VLMs), and XAI. This approach enhances interpretability, scalability, and clinical trust while improving diagnostic accuracy, particularly in resource-limited settings. The findings underscore the need for standardized datasets and clinically validated AI models to ensure real-world adoption and improved patient outcomes.

Keywords: Deep Learning, Medical Images, COVID-19, Convolutional Neural Network, Pneumonia and Explainable Artificial Intelligence. 

1.	Introduction

The study aims to research the problem of performing a correct medical diagnosis via web (Antunes, 2022) using deep learning techniques to identify the existence of pulmonary diseases like COVID-19 and pneumonia. COVID-19 is one of the deadliest diseases in the planet, that has been spreading around the world, causing in some cases severe respiratory problems and even death. The detection process of the SARS-CoV-2 can be improved (Echtioui et al., 2020). Traditional technologies are very laborious, time consuming, with high costs and tend to fail sometimes, being an example, cases where the virus has not spread enough, leading to detection failures at initial stages of the disease, which can affect future treatment. Pneumonia is a respiratory illness caused by an infection in one or both lungs. It can be caused by various microorganisms such as bacteria, viruses, fungi, and parasites (Kundu et al., 2021). Symptoms can include coughing, chest pain, fever, difficulty breathing, and fatigue. Pneumonia can be mild or severe, and treatment depends on the cause of the infection and the individual's overall health. Antibiotics are usually prescribed for bacterial pneumonia, while antiviral medications may be used for viral pneumonia. 
The study presents also an approach using a transformer-based VLM named contrastive language–image pretraining (CLIP) to predict the presence of COVID-19 and Pneumonia and a LLM called generative pre-trained transformer neo (GPT-Neo) to generate the medical report. The research aims to systematically review the state-of-the-art in deep learning-based methods for diagnosing COVID-19 and pneumonia using medical imaging, identifying research gaps and proposing future directions. To conduct this systematic literature review, an AI application called AI reviewer was developed allowing to fetch studies via a query, to answer research questions and generate the full SLR report using transformer based LLMs. To perform this SLR, we followed the preferred reporting items for systematic reviews and meta-analyses (PRISMA) guidelines. An initial search retrieved 5613 studies from databases such as Springer, Elsevier, IEEE, MDPI, Nature, ACM Digital Library, SAGE Journals, Taylor & Francis, IET Digital Library and others. After applying a first filter of inclusion and exclusion criteria, 189 studies were selected for detailed analysis. A second selection process was applied obtaining 129 papers focusing on the research questions after reading the full text and use of AI to answer research question and generate full report. The review focuses on comparing deep learning architectures, datasets, and evaluation metrics for COVID-19 and pneumonia detection. For this study the research objectives are: Investigate techniques and AI methods for detecting COVID-19 lesions in datasets of X-rays and CT scans of the thorax using a CNN to classify/identify if the disease is present with high accuracy (#Objective_1) .Analysis of studies and prototypes to predict and classify pneumonia from medical images of the lung (#Objective_2). Development of a web platform that shows the results of the analysis for the patients, generates a medical report and use of explainable artificial intelligence methods to provide transparency and confidence of the results obtained, in order to increase the confidence and credibility of the model to the final users (#Objective_3).
The research questions allow to refine the investigation according with the predefined objectives, the research paper will aim to find answers to the stated interrogations: How to improve the performance of the current detection processes of COVID-19 based in an X-ray or CT scan using deep learning (#Research_Question_1)? Which public datasets can be used in order to improve the accuracy of the prediction (#Research_Question_2)? How can pneumonia be detected via deep learning (#Research_Question_3)? How can web applications be developed in order to facilitate the diagnosis process and to ameliorate the explanations of the CNN previsions using explainable artificial intelligence (#Research_Question_4)?
The main contributions of this paper are to provide an innovative approach for performing SLRs with AI, analyse current detection technologies for identifying COVID-19 in X-rays and CT scans and pneumonia on X-rays using deep learning and provide features for web diagnosing with high accuracy and facilitate the work of the physician in understanding the results by providing medical reports. Section 2 introduces the research methodology used for performing the SLR. Section 3 describes the analysis and results obtained. The last section (Section 4) presents the conclusions, answers to the research questions, limitations and future work. This study provides a comprehensive systematic review of AI-driven COVID-19 and pneumonia diagnosis, discussing the strengths and limitations of existing models. The findings will help guide future research towards developing more accurate and explainable AI tools for medical imaging-based disease detection. 

2. Research Methodology

The research study follows the SLR guidelines proposed by (Kitchenham, 2004), widely adopted in the field of software engineering and artificial intelligence, ensuring rigor in the selection and analysis of studies as shown on Figure 1. The search was done taking in consideration the problem, the motivation, the research questions, the technologies that are going to be used, and keywords like COVID-19, pneumonia, deep learning and artificial intelligence. Mendeley was used to store and organize the selected articles. Parsifal helped managing inclusion/exclusion criteria and the CrossRef application programming interface (API) was used to automatically retrieve references from keywords.







Figure 1. Phases of the process of performing a SLR.

2.1 Planning the Review

The primary goal is to thoroughly examine the current advancements in the detection of COVID-19 through X-rays and CT scans and pneumonia via X-rays. The sources used were Springer, Elsevier, IEEE, MDPI, Nature, ACM Digital Library, SAGE Journals, Taylor & Francis, IET Digital Library and others. A quality assessment checklist is crucial for ensuring that the articles meet the required standards for inclusion in our study. Quality, in this context, refers to how effectively a study minimizes bias and ensures the reliability and validity of its findings. To enhance the quality of the systematic literature review, we have established the following criteria for evaluating the selected articles: Does the research compare different deep learning models using clearly defined performance metrics and evaluation criteria? Does the publication focus on deep learning applications in detecting COVID-19 through X-rays and CT scans and pneumonia via X-rays, providing relevant insights into these applications? Does the publication assess the effectiveness and accuracy of deep learning models for detecting COVID-19 and pneumonia in medical imaging? Is the scope of the evaluation model clearly defined, such as whether it focuses on individual image analysis, clinical decision support, or both? Does the publication identify the key factors that influence the performance of deep learning models in medical image analysis, particularly for detecting COVID-19 and pneumonia? Does the publication critically examine the perspectives of different authors on the significant factors contributing to the success of deep learning models in these medical applications? Is the classification presented via web? If it is, do they show XAI? Which web modules were introduced?
A snowballing technique was applied to identify additional studies by reviewing references from key papers. Table 1 shows some of the sub strings used to fetch data.

Table 1. Number of articles per search string
Search String (SQL Clause)	Number of articles
Where (title LIKE 'Computed Tomography ' OR title LIKE 'X-Ray' OR title LIKE 'Healthcare') AND (theme LIKE 'Artificial Intelligence' OR 'Deep Learning')	8
Where (title LIKE 'Pneumonia' OR title LIKE 'X-Ray' OR title LIKE 'Healthcare') AND (theme LIKE 'Artificial Intelligence' OR 'Model' OR 'Deep Learning')	14
Where (title LIKE 'Web Application' OR title LIKE 'X-Ray' OR title LIKE 'Healthcare') AND (theme 'LIKE Deep Learning')	15
Where (title LIKE 'Web Application' OR title LIKE 'Computed Tomography OR title LIKE 'X-Ray' OR title LIKE 'COVID-19' OR title LIKE 'Pneumonia') AND (theme LIKE 'Deep Learning)	23

2.2 Conducting the Review

On the initial stage, a total of 5613 studies were selected through a combination of two strategies. The first strategy involved using a Python-based application (source code available at: AI Reviewer) developed by the authors, which automated the process of study retrieval. The second strategy utilized a search string within the Mendeley and Parsifal applications to conduct a comprehensive search. The created system utilizes Algorithm 1 for paper selection, integrates studies retrieved through a defined query embedded in the Python code, ensuring an efficient and structured collection of relevant papers for further analysis.
Algorithm 1: Reference Retrieval Web Application

Input:
User query submitted via a web form.
Output:
Generated research content sections, a list of academic references, and a rendered result page.
Steps:
import necessary libraries
initialize route '/'
If request is POST then
   extract user query
   fetch references by querying the CrossRef API
   extract and store reference details
   render result.html with generated sections and references
End If
Ultimately, Figure 2 illustrates the efficiency and effectiveness of this user interface in supporting the research process for #Research_Question_1. The user interface also emphasizes simplicity and clarity in its design, ensuring that researchers can easily navigate through the process without requiring extensive technical expertise. The straightforward layout presents the results in a well-organized structure, enabling users to quickly review details of the retrieved papers. 
  
Figure 2. Interface of the application to obtain references concerning the research question via AI.

For the references, the application defines a function that queries the CrossRef API with the user's input. If the API response is valid, it extracts details such as the title, authors, publication year, journal name, and uniform resource locator (URL) for each research question. 
After initially identifying 5,613 papers, Filter 1, as shown in Table 2, was applied to refine the selection, shortlisting to 189 studies. For relevance, studies must directly address the research questions concerning AI applications in detecting COVID-19 and pneumonia through medical imaging. The study focus criterion ensures that only studies explicitly discussing machine learning methodologies for detection are included. Data availability is a crucial factor; studies that provide access to open-source code, datasets, or detailed methodologies enabling replication and validation of results were prioritized. Ethical considerations are integral to the quality of deep learning research, and studies addressing biases in training data, fairness, and privacy concerns are prioritized. Regarding publication type, only peer-reviewed articles published in reputable journals or conferences were retained, ensuring high standards of academic rigor and scientific validation. The model interpretability criterion focuses on studies that explored techniques for enhancing the transparency and explainability of deep learning models, such as transfer learning, hyperparameter tuning, and the integration of clinical domain knowledge. Transparency in the research process is essential; studies emphasizing reproducibility, transparent reporting of methodologies, and clear documentation of results were included. The clinical impact of the study is also a determining factor. Only studies addressing practical deployment challenges, such as balancing computational efficiency with diagnostic accuracy, were included, as they provide valuable insights for real-world application. Duplicate studies were identified and excluded to maintain the uniqueness of the dataset. Language is another selection criterion; studies published in English are retained. Lastly, the methodology criterion ensures that only studies employing a structured, rigorous approach, such as design science research methodology, or a clearly defined experimental setup were included. 

Table 2. First filter applied, shortlisting from 5613 to 189 studies.
Filter 1:		
Criteria Type	Inclusion Criteria	Exclusion Criteria
Relevance	Directly addresses research questions related to deep learning in detecting COVID-19 and pneumonia using medical imaging.	Does not focus on deep learning-based detection of COVID-19 or pneumonia or is unrelated to medical imaging.
Study Focus	Explicit focus on machine learning methodologies for COVID-19 or pneumonia detection.	Focuses on other methodologies or conventional diagnostic techniques.
Data Availability	Provides access to open-source code, datasets, or detailed methodologies for replication and validation.	Does not provide access to code, datasets, or methodological details.
Ethical Considerations	Discusses biases in training data, fairness, and privacy concerns.	Does not address ethical dimensions or concerns such as biases or privacy.
Publication Type	Peer-reviewed articles published in prestigious journals or conferences.	Non-peer-reviewed articles or low-quality publications.
Model Interpretability	Explores interpretability methods like transfer learning, hyperparameter tuning, and integration of clinical knowledge.	Does not discuss methods to enhance model interpretability.
Transparency	Emphasizes reproducibility and transparency in deep learning research.	Does not emphasize transparency or reproducibility.
Impact on Clinical Settings	Addresses real-world deployment challenges, such as computational efficiency vs diagnostic accuracy.	Does not consider real-world deployment challenges or practical applications.
Irrelevant	Relevant to the specific research questions and context.	Irrelevant to the research questions or context.
Non-Peer Reviewed	Final peer-reviewed articles only.	Non-peer-reviewed articles or unpublished works.
Duplicate Studies	Unique and non-duplicated studies.	Duplicated or repeated studies in the dataset.
Language	Published in English (or other predefined languages).	Non-English publications (if applicable).
Methodology	Uses a structured methodology, such as design science research methodology.	Does not follow a clear, structured methodology or lacks sufficient research rigor.

Filter 2 described on Table 3 was applied to narrow down the selection from 189 to 129 studies. The inclusion criteria emphasized peer-reviewed journal articles or conference papers, ensuring that only studies that utilized publicly available datasets or provided detailed descriptions of their datasets were included. Performance metrics such as accuracy, sensitivity, and specificity were important for inclusion. Studies that compared different deep learning models with clearly defined performance metrics were also included. Researches that identified key factors influencing model performance, such as dataset size, preprocessing techniques, and neural network architectures, were prioritized. Additionally, studies assessing model interpretability using techniques like XAI and Grad-CAM were analysed. For the web application functionality, only studies that explored web applications for uploading X-rays or CT scans for disease detection with advanced deep learning models were included. Clinical relevance was another key factor, with studies offering clinically validated results and detailed analysis of architecture, preprocessing pipelines, and interpretability mechanisms being included. Transparency in methodology was also a crucial criterion, with studies offering access to code, datasets, or detailed processes being prioritized. Lastly, generalizability was important, with studies that demonstrated broad relevance across diverse imaging conditions, datasets, or patient demographics being included.

Table 3. Second filter applied, shortlisting from 189 to 129 studies.
Filter 2:		
Criteria	Inclusion	Exclusion
Datasets	Studies using publicly available datasets or providing detailed descriptions of the datasets used	Studies lacking information on datasets or using proprietary datasets without generalizability
Performance Metrics	Studies reporting performance metrics such as accuracy, sensitivity, and specificity	Studies without performance evaluations
Evaluation of Deep Learning Models	Comparison of different deep learning models with clearly defined performance metrics	Studies that do not compare different models or lack clear performance evaluations
Scope of Evaluation	Clear definition of evaluation scope (individual image analysis, clinical decision support, or both)	Lack of clarity in the scope of the evaluation
Factors Influencing Model Performance	Identification of key factors influencing model performance in medical image analysis (e.g., dataset size, preprocessing techniques, neural network architectures)	Studies that do not identify or examine the critical factors influencing model performance
Model Interpretability	Studies that assess and present the interpretability of models (e.g., XAI, Grad-CAM)	Studies that do not address model interpretability or explanation of predictions
Web Application Functionality	Research on web applications for uploading X-ray or CT scans for disease detection with advanced deep learning models	Studies lacking web-based interfaces, focusing only on desktop/mobile applications, or failing to provide clinical relevance or real-world data validation
Clinical Relevance	Studies offering clinically relevant and validated results, including a detailed analysis of architecture, preprocessing pipelines, and interpretability mechanisms	Studies that do not involve X-rays or CT scans or lack real-world validation of their models
Publication Transparency	Studies offering transparency in methodologies (e.g., access to code, datasets, or detailed processes)	Studies with minimal citations, insufficient context, or lacking transparency in methodology
Robust Methodologies	Studies that employ robust methodologies (e.g., Design Science Research, computational efficiency considerations)	Studies with weak methodologies or insufficient rigor in research design
Generalizability	Studies with broad relevance and generalizability across diverse imaging conditions, datasets, or patient demographics	Studies limited to specific regions, institutions, or proprietary datasets with limited generalizability

This filtering process resulted in a refined dataset of 129 studies (see Figure 3). In alignment with predefined quality criteria, publications were selected that provided comprehensive reviews of deep learning models specifically developed for the detection of COVID-19 in X-rays and CT scans, as well as pneumonia detection in X-rays. 
 
Figure 3. Diagram illustrating the flow of information for the systematic review in this study.

Data extraction was performed after applying filter 2. The selected studies were obtained after reading the full paper and code testing, 29 studies were related to #Research_Question_1, 27 to #Research_Question_2, 41 for #Research_Question_3 and 32 related to #Research_Question_4.
Figure 4 illustrates the distribution of the 129 selected studies by year of publication and corresponding citation counts, highlighting the academic impact and influence of each article. High citation counts typically indicate substantial contributions to the field, with findings widely recognized and referenced in subsequent research. Conversely, lower citation counts may reflect newer studies or those with limited reach.
 
Year	Articles	Citations
2008	1	45
2010	1	548
2011	1	1
2015	1	130
2016	1	91
2017	3	23883
2018	2	3150
2019	4	689
2020	38	14253
2021	30	3061
2022	28	845
2023	16	310
2024	2	1
2025	1	0
Figure 4. Graph of the distribution of the number of articles (left) and citations (right) per year as well as a table of this distribution during the years.

Figure 5 examines the temporal distribution and publisher-specific patterns in the selected academic publications spanning from 2008 to 2025, with particular emphasis on the quantitative assessment of publication volumes across multiple publishing entities. The analysis encompasses data visualization through various bar chart representations. The analytical approach employed in this study utilizes a multi-dimensional visualization framework, incorporating distinct representations: articles by publisher type and year and total articles by publisher. These visualizations were generated using the Recharts library within a React.js framework, ensuring optimal data representation and interpretability. Springer emerges as the predominant publisher, with approximately 30 publications throughout the analysed period. Others/Unknown sources (31 publications), Elsevier (24 publications), and IEEE (22 publications). 
  










Articles by Publisher (Top 10)
Publisher	Number of Articles
Other	31
Springer	30
Elsevier	24
IEEE	22
MDPI	11
Nature	4
ACM Digital Library	2
SAGE Journals	2
Taylor & Francis	1
SPIE Digital Library	1
IET Digital Library	1
Figure 5. The graphs from upper left, upper right and middle right represent the distribution of the number of articles selected by publisher and year, the graph on the middle left and bottom table display the number of articles by publisher after applying the second filter.

Figure 6 examines the distribution of the citations across major publishers, based on the filtered dataset. The quantitative analysis reveals a significant disparity across publishers. ACM Digital Library emerges as the dominant publisher with 23,843 citations, Elsevier with 10,404 publications, followed by Springer with 5,478 publications, while other publishers account for 2,041 publications. The total volume of citations selected to answer the research questions is 46,869. While this analysis provides valuable insights into publisher distribution patterns, several limitations should be noted. The aggregation of multiple publishers into the "Other" category may mask important patterns among smaller publishers. Additionally, temporal trends and subject-specific distribution patterns are not captured in this dataset. 
														
Publisher	Citations
Other	2041
Elsevier	10404
Springer	5478
IEEE	2169
MDPI	816
ACM Digital Library	23843
SAGE Journals	121
Taylor & Francis	366
Nature	1596
IET Digital Library	2
SPIE Digital Library	33

Figure 6. On the left a table of the number of citations by publisher and on the right the graphical representation.

Once all the papers were read, the AI application developed by the authors was applied to each of the selected studies. The AI tool was designed to enhance the research process by automatically processing and analysing the content of each paper. This included extracting key pieces of information such as main findings, statistical results, methodologies used, and any conclusions drawn that were directly related to the research questions. For each research question, the AI tool was applied to all the correspondent selected studies, allowing for a more systematic and consistent analysis across all papers. The application was programmed to identify patterns, common themes, and significant findings, which it then used to generate a response to each research question based on the combined data from all the papers.
The final step in the process was the generation of a full report for each research question. After the AI application had processed all selected papers, it produced a detailed report for each research question, which summarized the answers and insights derived from the papers. The reports were structured to provide clear, concise answers to the research questions, incorporating findings from all relevant studies. The AI-generated reports also included additional analysis. The use of Filter 2 and the AI application ensured that the analysis was not only comprehensive and thorough but also efficient, allowing for high-quality insights to be derived from a large body of literature in a relatively short period.

2.3 Reporting the Review

The reporting of the review is performed on sections 3 and 4 with the use of the developed application AI reviewer.

3. Analysis and Results Obtained After Using the Research Methodology

A range of studies (see table 2) have demonstrated the potential for automatic diagnosis of COVID-19 on CT scans and X-rays and pneumonia via X-rays. (Micallef et al., 2022) and (Polat et al., 2021) both achieved high accuracy in detecting COVID-19 in chest CT scans using convolutional neural networks, with Micallef achieving 96.31% accuracy and Polat achieving 93.26% accuracy. (Kumar et al., 2022) further expanded on this by using deep learning techniques to achieve an accuracy of over 95% in differentiating COVID-19 positive cases from CT-scan and X-ray images. (Elkamouny & Ghantous, 2022) developed a web tool that uses machine learning models to diagnose COVID-19 and pneumonia with an average testing accuracy of 95% for the pathological condition network (PCN) classification. 
Table 4 shows a more in-depth analysis of some of the selected studies concerning the detection of COVID-19 in X-rays and CT scans and pneumonia on X-rays.

Table 4. Analysis of studies concerning the detection of COVID-19 and pneumonia on medical images
Paper	Abstract summary	Main findings	Outcome measured
Automatic Detection of COVID-19 Pneumonia in Chest Computed Tomography Scans Using Convolutional Neural Networks
Neil Micallef +3
2022 IEEE 21st Mediterranean Electrotechnical Conference (MELECON) 2022
0 citations
(Micallef et al., 2022)
A machine learning-driven approach automatically detects pulmonary pathological features caused by the Coronavirus infection in chest CT images.	The study proposes a machine learning approach for automatic detection of pulmonary pathological features caused by Coronavirus infection in chest Computed Tomography images. The model achieved an accuracy of 96.31% on the testing segment of the dataset.	Accuracy of the machine learning model in detecting pulmonary pathological features in chest Computed Tomography images (96.31%)
Detection of COVID-19 on Localized Ct-scan Images Using Deep Learning Convolution Neural Network
S. Widodo +2
International journal of advanced engineering and management research 2022
1 citation
(Widodo et al., 2022)
	The current method used to diagnose COVID-19 from CT scan images is by studying the 2-D CT scan image data set using naked eye, then interpreting the data one by one.	The study aimed to develop a COVID-19 detection application on localized CT-Scan images using a Deep Learning Convolution Neural Network (CNN) with a pre-trained model residual network (ResNet) 50, achieving high accuracies of 92.5% to 98% in different test scenarios.	Accuracy of COVID-19 detection on localized CT-Scan images using Deep Learning Convolution Neural Network: 92.5%, 95%, and 98%
Clinical Characteristics of the COVID-19 Patients with Pneumonia Detected by Computerized Tomography but Negative for Infiltration by X-ray
D. Acharya +6
Healthcare
2020
2 citations
(Acharya et al., 2020)
CT scans should be performed on COVID-19 patients negative for a pneumonic lung lesion by CXR who are suspected to be pneumonic on clinical grounds.	Patients with pneumonia detected by CT were older, had more comorbidities, and serum albumin level and preexisting stroke were independent predictors of pneumonia detection by CT.	Presence of pneumonia detected by CT in COVID-19 patients without an active lesion detected by CXR
Pneumonia and COVID-19 Detection using Convolutional Neural Network
Prof. M. R. Gorbal 
International Journal for Research in Applied Science and Engineering Technology
2022
1 citation
(Militante et al., 2020)
A deep neural network-based model to triage patients for appropriate testing is proposed.	Using chest X-Rays for COVID-19 detection can aid in quarantining high-risk patients while awaiting test results. The proposed AI model, CovidAID, demonstrates a 90% accuracy in detecting COVID-19 infections on chest X-Rays. This approach can help prioritize patients for further RT-PCR testing.	Accuracy of the CovidAID model in detecting COVID-19 infections on Chest X-Ray images (90%)
Pneumonia Classification for COVID-19 Based on Machine Learning
Mahmoud Elkamouny +1
2022 2nd International Mobile, Intelligent, and Ubiquitous Computing Conference (MIUCC)
2022
3 citations
(Elkamouny & Ghantous, 2022)
A web tool was developed to help physicians upload and analyse x-ray images quickly using several machine learning models in the backend to diagnose COVID-19 or pneumonia with its types.	The study developed machine learning models with high testing accuracies for classifying COVID-19, pneumonia, and their types, potentially improving the efficiency of healthcare systems in diagnosis.	Testing accuracy of machine learning models for differentiating between normal, COVID-19, and pneumonia (PCN) as well as between viral and bacterial pneumonia (BV)
Automatic Diagnosis of Covid-19 Related Pneumonia from CXR and CT-Scan Images
N. Kumar +3
Engineering, Technology & Applied Science Research
2022
22 citations
(Kumar et al., 2022)
CT-scan and X-ray images can be used for early detection of Covid-19 related pneumonia.	Deep learning techniques can achieve an accuracy of more than 95% in diagnosing Covid-19 related pneumonia. Eight CNN-based deep learning models were used to differentiate Covid-19 positive cases in X-rays and CT-scans. The proposed models showed the ability to differentiate Covid-19 positive cases effectively.	accuracy of deep learning models in diagnosing pneumonia using CT-scan and X-ray images
Automatic detection and localization of COVID ‐19 pneumonia using axial computed tomography images and deep convolutional neural networks
Hasan Polat +3
International journal of imaging systems and technology (Print)2021
12 citations
(Polat et al., 2021)
A deep convolutional neural network-based model can automatically detect patterns related to lesions caused by COVID-19 from chest computed tomography images.	The main findings include the high diagnostic accuracy of 93.26% achieved by the deep CNN-based model in detecting COVID-19 lesions, successful automatic localization of COVID-19 pneumonia with high resolution, and the importance of automated diagnostic systems in combating the pandemic.	Diagnostic accuracy (93.26%), Sensitivity (93.27%), Specificity (93.24%)

Conducted as a mapping study, the review aimed to identify research gaps, particularly highlighting the limited use of large language models (LLMs) and vision-language models (VLMs) in comparison to the more prevalent application of deep learning strategies. While deep learning has been widely explored, the adoption of LLMs and VLMs in medical imaging remains scarce, presenting an opportunity for advancing diagnostic accuracy and addressing unmet needs in the field.
Figure 7 presents the longitudinal analysis of the mapping process, which reveals evolving patterns in research focus over the years. On the 129 selected studies, between 2016 and 2026, COVID-19-related articles showed the highest volume, with 95 publications, reflecting the global emphasis on addressing the pandemic. Pneumonia-related research followed with 47 selected studies, while deep learning-focused studies accounted for 41 publications. Notably, research addressing dataset training was the least represented, with only 8 publications, signalling an area where additional efforts are necessary.
Studies leveraging these advanced models could further enhance the accuracy of diagnostic predictions, particularly in identifying and analysing complex patterns in X-ray images associated with COVID-19. By bridging this gap, future research can capitalize on the interpretability and feature extraction capabilities of these models, contributing to more reliable and robust diagnostic tools in medical imaging.
Overall, this analysis underscores the progress made in using computational models for COVID-19 and pneumonia highlighting the untapped potential of LLMs and VLMs. 
Year:	Number of COVID-19 related Articles	Number of Pneumonia related articles	Number of Deep Learning related articles	Number of Dataset training articles
2016	0	1	0	0
2017	0	0	0	0
2018	0	1	1	0
2019	0	2	2	0
2020	35	6	9	3
2021	26	15	9	3
2022	20	11	10	0
2023	11	9	8	1
2024	2	2	1	0
2025	1	0	1	1
Figure 7. On the left a table of the mapping of the selected articles by year and on the right the graphical representation.

The developed AI application was used to report the reviews, focusing specifically on the four research questions. The application utilizes Algorithm 2 to generate answers to the research questions. After uploading the PDF version of a paper or pasting the full content of the article into a text box, the algorithm processes the text and generates comprehensive responses to the research questions inputted by the final user. Figure 8 illustrates the process of obtaining a research answer. 
 
 
Figure 8. Answer to a research question after copy and pasting the full text of a scientific article.
Algorithm 2 begins by accepting a research question and a text or the PDF file. The Flask application has the settings configured for file uploads. It defines which file types are allowed for upload, such as PDF and text files. The system loads pre-trained models and tokenizers for the transformers-based bidirectional and auto-regressive transformers (BART), GPT-2, and GPT-Neo models. These models are used to generate answers to specific research questions posed by users, based on the content of the uploaded document. In the code of the application there is a function called allowed_file that checks whether the uploaded file is of an acceptable type. 
Algorithm 2: Answer Generation and Reference Extraction from Uploaded PDF
Input:
question: A string containing the research question to be answered.
pdf_text: A string containing the text extracted from a PDF file, or it may be simulated if the file is uploaded.
uploaded_file: A file object representing the uploaded PDF or text file.
max_length: An integer specifying the maximum length of the generated answer (optional, default = 1500).
min_length: An integer specifying the minimum length of the generated answer (optional, default = 700).
Output:
bart_answer: A string containing the answer generated by the BART model.
gpt2_answer: A string containing the answer generated by the GPT-2 model.
gpt_neo_answer: A string containing the answer generated by the GPT-Neo model.
references: A list of references extracted from the text, formatted according to typical citation patterns.
Steps:
If the file extension is in pdf or txt,
   Return True.
   Else
      Return False.
   End Else
End If
Define the extract_references function to extract references from the text.
Input: pdf_text.
Use a regular expression to find citation patterns, such as [1].
Set matches to the list of references found by the regular expression.
If no matches are found,
   Return the default list ["No references found."].
End if
Define the generate_answer function to generate an answer using a specified model.
Input: model_name, pdf_text, question.
Retrieve the appropriate model and tokenizer based on model_name.
Prepare the input text by concatenating the research question with the context from the PDF.
If the input text exceeds the token limit of the model,
   Truncate the input text to fit the model’s maximum token length.
End if
Use the model to generate an answer based on the prepared input text.
Return the decoded answer from the model.
Define the process route to handle the user’s request.
Input: question, pdf_text, uploaded_file.
If either question or both pdf_text and uploaded_file are missing,
   Return an error response indicating that these inputs are required.
End if
If a valid file is uploaded,
Save the file to the server, and simulate PDF text extraction.
Extract references from the pdf_text using the extract_references function.
For each model in [BART, GPT-2, GPT-Neo],
   Generate answers using the model.
End for
Render and return the result template with the generated answers and extracted references.
Define the health_check route to verify the health status of the service.
Return a JSON object indicating the health status, which should show "running" if the service is operational.
Start the Flask application.
The generate_answer function is defined to produce answers to the research questions. This function takes in three inputs: the model’s name, the text of the PDF, and the research question itself. Based on the model selected (BART, GPT-2, or GPT-Neo), the application retrieves the corresponding pre-trained model and tokenizer from the transformer’s library. It then prepares the input by combining the research question with the context from the document. The model is then used to generate an answer, which is returned after being decoded from the model’s output.
The references are then extracted using the extract_references function, and the system generates answers for each model (BART, GPT-2, and GPT-Neo). These answers, along with the extracted references, are rendered in a result page for the user to view.
Finally, the code includes a health check function to monitor the status of the Flask application. This route simply returns a JSON response indicating that the service is running, which is useful for ensuring the application is operating correctly. 
Figure 9 illustrates the user interface of the developed AI tool designed to generate a comprehensive report. To begin, the user must provide the title of the report, followed by a research question and a corresponding research objective. In addition to these essential elements, the user is also required to include a brief mention or description of the topic under consideration. Once all of these details are entered, the AI tool processes the input and generates a full report, complete with relevant references. 
Algorithm 3 begins with the initialization of the necessary transformer-based AI models. These models include GPT-2, which is used for text generation, and BART, which is responsible for summarization tasks. Additionally, a question-answering pipeline is loaded to help answer any research questions the user may provide. The references are retrieved by calling an external API, specifically the CrossRef API, which provides academic papers related to the given topic. With the references in hand, the system proceeds to generate the various sections of the literature review. The first section generated is the abstract. Using GPT-2, a short abstract is created that provides a brief summary of the paper based on the provided title and objective. Following the abstract, the introduction, theoretical background, and development sections are generated by summarizing the first few references retrieved. These summaries are generated using the BART transformer model, which is designed to condense the content of the references into shorter, more digestible summaries. Once the sections related to the introduction and background are summarized, the next step is to answer the research question. The question-answering pipeline is used to extract a relevant answer by analysing the theoretical background and development sections generated earlier. The context from these sections helps the pipeline formulate a detailed answer to the research question provided by the user. After answering the research question, the conclusion section is generated. This section is also created using GPT-2, which is asked to summarize the findings of the review and provide a concluding statement based on the description of the topic. The conclusion is designed to tie together the information presented throughout the report. All of these sections, the abstract, introduction, theoretical background, development, research answers, and conclusion are then compiled into a single web document. The document is structured with headings for each section, making it easy for the reader to navigate through the various parts of the report. Finally, the system returns the complete, multi-page report to the user. 
 


 
 	  
 
Figure 9. User interface for generating a scientific report.

Algorithm 3: Generation of SLR Report Using AI Pipelines
Input:
Title: The title of the research paper.
Question: The research question to be answered.
Objective: The research objective that guides the study.
About: A description or topic about which the SLR is generated.
Output:
A multi-page SLR report with various sections including the abstract, introduction, theoretical background, development, research answers, tests, conclusion, and references.
Steps Generation of the SLR Report Using AI Pipelines:
Load GPT-2 for text generation. 
Load BART for summarization. 
Load the QA pipeline for answering questions.
Retrieve User Inputs: Title, Question, Objective, About.
If any of the required inputs are missing
   return an error message. 
End If
Call `fetch_references` with the "About" input.
If no references are found
   return a default message. 
End If
Generate Section: Abstract: Use GPT-2 to generate a short abstract based on the Title and Objective. 
Generate Sections: Introduction, Theoretical Background, and Development.
For each reference in the first few fetched references
   Summarize the reference using the `summarize_references` function. 
End For
Research Answers: Use the QA pipeline to answer the research question, using the Theoretical Background and Development sections as context.
Conclusion: Use GPT-2 to summarize findings and write the conclusion based on the "About" input.
Combine all generated sections into an HTML document.
Return Result.
If errors occur at any stage
   return an error message
End If 
If successful
   return the generated report in multiple pages.
End If

3.1 Analysis of the Public Datasets

The CNNs require large amounts of data, which have to be prepared before performing training. Testing and validation datasets are important aspects, because they can increase the accuracy and performance of the model. To perform classification will be required to label the data for training purposes, in order to determine if a medical image has Covid, pneumonia or none (normal) will be required examples of these medical images for cases with and without the disease. During recent times, many open-source public datasets of COVID-19 have been placed online (Mohamadou et al., 2020) (see Figure 10).
 
Figure 10.  List of open-source datasets (Mohamadou et al., 2020).
Darwin-Labs has a huge online dataset of COVID-19 chest X-rays which is larger than many datasets used for COVID-19 related neural networks (Zhang, 2020). Medical images like CT scans or X-rays of the thorax can be used for automated processes of detecting the SARS-CoV-2 virus, which can be as accurate or better than the one done by a human, consuming less time and at cheaper costs when compared with the processes done by laboratories (Shuja et al., 2021). There are several publicly available datasets to detect COVID-19 and Pneumonia. COVID-19 Radiography Database (Rahman, 2022) (Dataset 1) released chest X-ray images for COVID-19 positive cases along with normal and viral Pneumonia images, in example, 3,616 COVID-19, 10,192 normal, 6,012 Lung Opacity (Non-Covid lung infection), and 1345 viral Pneumonia images and corresponding lung masks. The extensive COVID-19 X-Ray and CT chest images dataset CoV-Healthy-6k (El-Shafai, 2020) (Dataset 2 for X-rays and Dataset 5 for CT scans) contains X-rays and CT scans of healthy individuals and people with the COVID-19 virus, where several X-rays and CT scans can be found with and without COVID-19. Concerning the CT scans were used 5427 with COVID-19 and 2628 without, X-ray 4,044 with Covid and 5,500 noncovid. The Curated Dataset for COVID-19 Posterior-Anterior Chest Radiography Images (X-Rays) (Sait, 2021) (Dataset 3) contains 1281 COVID-19 X-Rays, 3270 Normal X-Rays, 1656 viral-pneumonia X-Rays, and 3001 bacterial-pneumonia X-Rays. The COVID-19 lung CT Scans dataset (Aria, 2021) (Dataset 4) has more than 8,000 images of CT scans with COVID-19 and without. The images in this dataset were gathered from radiology departments at teaching hospitals in Tehran, Iran. The COVID-19 status of patients in the dataset was verified using reverse transcription-polymerase chain reaction (RT-PCR) tests. 
The SARS-CoV-2 CT-scan dataset (Angelov & Soares, 2020) (Dataset 6) is composed of 2,482 CT scan images, which is divided between 1,252 for patients infected by SARSCoV-2, and 1,230 CT scans for non-infected by SARS-CoV-2 patients, but presented other pulmonary diseases. The data was collected from hospitals in São Paulo, Brazil. The Chest X-ray (COVID-19 & Pneumonia) dataset (Dataset 7), has in total 6432 x-ray images, containing 3,418 X-rays with pneumonia and 1,266 normal. The Labelled Optical Coherence Tomography (OCT) and Chest X-Ray Images for Classification dataset (Dataset 8) was compiled by University of California San Diego. The latest version of this dataset is composed of 5,856 X-ray images. It was divided into a training set consisting of 3,883 X-rays corresponding to cases of pneumonia and 1,349 X-rays without detected pathologies, and a test set with 234 images labelled as pneumonia and 390 without detected pathologies. The chest X-Ray Images (Pneumonia) dataset (Mooney, 2018) (dataset 9) has 1,341 images labelled as normal for training, and 3,875 X-rays with pneumonia, including validation and tests there are in total 5,856. The dataset comprises three main folders (train, test, validation) with subfolders for each image category (Pneumonia/Normal), totalling 5,856 JPEG X-ray images across two categories. These chest X-ray images (anterior-posterior) were sourced from paediatric patients aged one to five at Guangzhou Women and Children’s Medical Centre as part of routine clinical care.
Table 5 shows the number of images used for each of the datasets applied in this research, mentioning how many medical pictures have the diseases COVID-19 and pneumonia and how many are X-rays and also the number of CT scans. 

Table 5. The Datasets used on the research concerning CT scans and X-rays and the identification of cases with COVID-19, cases with pneumonia and normal case.
Dataset	X-Ray	CT	X-ray
	Covid	Noncovid	Covid	Noncovid	Normal	Pneumonia
COVID-19 Radiography Database (Rahman, 2022) (Dataset 1) 
3616	10192			10192	6012
The extensive COVID-19 X-Ray and CT chest images dataset CoV-Healthy-6k (El-Shafai, 2020)  (Dataset 2 for X-rays and Dataset 5 for CT scans)	4044	5500	5427	2628		
Curated Dataset for COVID-19 Posterior-Anterior Chest Radiography Images (X-Rays) (Sait, 2021) (Dataset 3)
1281	3270				4657
COVID-19 lung CT Scans dataset (Aria, 2021) (Dataset 4)
		7496	944		
SARS-CoV-2 CT-scan dataset (Angelov & Soares, 2020) (Dataset 6)
		1252	1230		
Chest X-ray (COVID-19 & Pneumonia) dataset (Prashant, 2020) (Dataset 7)
Train: 460
Test:
116			chest X-ray (COVID-19 & Pneumonia) dataset [26]
Train: 1266
Test: 317	Train: 3418
Test: 855
Labelled Optical Coherence Tomography  and Chest X-Ray Images for Classification dataset (Kermany, 2018) (Dataset 8)
			labelled Optical Coherence Tomography  and Chest X-Ray Images for Classification dataset  [27]
Train: 1349
Test: 234	Train: 3883
Test: 390
The chest X-Ray Images (Pneumonia) dataset (Mooney, 2018) (dataset 9) [28]
	chest X-Ray Images (Pneumonia) dataset  [28]
		Train: 1341
Test: 234
Val: 8	Train: 3875
Test: 390
Val: 8


To ensure the trained models generalize well and do not overfit to specific datasets, several techniques can be employed. Data augmentation, which includes rotation, flipping, contrast adjustment, and noise addition, can be used to artificially expand the dataset and enhance model robustness. Transfer learning, which leverages pre-trained models on large-scale medical image datasets before fine-tuning them on COVID-19 and pneumonia images, can improve feature extraction and prevent overfitting. Regularization methods such as dropout, batch normalization, and L2 regularization can be applied to reduce overfitting and enhance model generalization. Employing k-fold cross-validation ensures that the model is tested across multiple subsets of the dataset. Ensemble learning, which combines predictions from multiple models, can reduce variance and improve overall performance, preventing reliance on a single model’s learned biases. The primary contributions of this research to the field of AI-based medical diagnostics include a comprehensive dataset analysis, highlighting their strengths and limitations. 

3.2 Performance of Models in Detecting COVID-19 in X-ray Images

In order to achieve #Objective_1 several studies were analysed and the results compared (see Table 7) of the systematic literature review performed concerning the detection of COVID-19 on X-rays, presenting the accuracy obtained for different developed models. The study by (Shankar et al., 2021) presents the BMO-CRNN model, which combines a Barnacle Mating Optimization (BMO) algorithm with a Cascaded Recurrent Neural Network (CRNN), experimental results demonstrated that the BMO-CRNN model achieved an accuracy of 97.31%, with a sensitivity of 97.01%, specificity of 98.15%, and an F-measure of 97.73%, outperforming several state-of-the-art methods..
 
Table 6. Studies using deep learning to detect COVID-19 on X-rays and the results obtained.
Study	Used Architectures	Architecture that showed higher results	Results
(Apostolopoulos & Mpesiana, 2020).
VGG19, MobileNetV2, Inception, Xception, InceptionResNetV2	MobileNetV2	Accuracy = 96.78%
(Shankar et al., 2021)
BMO-CRNN	BMO-CRNN	Accuracy = 97.31%
(Hall et al., 2020)
VGG16 + ResNet50	VGG16 + ResNet50 + custom CNN	Accuracy = 89.2%
(Tang et al., 2020)
CNN	CNN	Accuracy = 94.64%
(Minaee et al., 2020)
ResNet18, ResNet50, SqueezeNet, DenseNet-121	SqueezeNet	Sensitivity = 98%, Specificity = 92.9%
(Afshar et al., 2020)
Covid-CAPS	Covid-CAPS	Accuracy = 95.7%
(Ahsan, et al., 2020)
VGG16, InceptionResNetV2, ResNet50, DenseNet201, VGG19, MobilenetV2, NasNetMobile, and ResNet15V2	NasNetMobile	Accuracy = 93.94%
(Hemdan et al., 2020)
VGG19, Xception, ResNetV2, DenseNet201, InceptionV3, MobileNetV2, InceptionResNetV2	VGG19, DenseNet	F1-Score = 0.91
(Ozturk et al., 2020)
Modified Darknet	Modified Darknet	Accuracy = 98%
(Khan et al., 2020)
Xception	Xception	Accuracy = 94%
(Chandra et al., 2021)
ACoS system	ACoS system	Accuracy = 91.33%
(Pandit et al., 2021)
VGG16	VGG16	Accuracy = 96%
(Arias-Londono et al., 2020)
Grad-Cam	Grad-Cam	Accuracy = 91.5%
(Yamac et al., 2021)
CSEN-based classifier	CSEN-based classifier	Sensitivity = 98% Specificity = 95%
(Wang et al., 2020)
Covid-Net	Covid-Net	Accuracy = 93.3%
(Abbas et al., 2020)
DeTrac	DeTrac	Accuracy = 93.1%
(Toraman et al., 2020)
CapsNet	CapsNet	Accuracy = 97%
(Narayan et al., 2022)
Xception	Xception	Accuracy = 97%
(Hu et al., 2020)
MD-Conv	MD-Conv	Accuracy = 93.4%
(Ismael & Şengür, 2021).
Novel CNN Model	Novel CNN Model	Accuracy = 91.6%
(Farooq & Hafeez, 2020)
Fine-tuned ResNet50	Fine-tuned ResNet50	Accuracy = 96.23%
(Ahmad et al., 2023)
ULTRA-X-COVID	ULTRA-X-COVID	Accuracy = 94.3%,

The research of (Ahmad et al., 2023) presented the ULTRA-X-COVID, a specialized deep neural network developed for automatically detecting COVID-19 infections using ultra-low-dose X-ray images. The study encompassed a multinational and multicentre dataset comprising 30,882 X-ray images collected from about 16,600 patients across 51 countries. Notably, there was no overlap between the training and test sets. Data analysis was conducted between April 1, 2020, and January 1, 2022. To assess the model's efficacy, multiple metrics such as area under the receiver operating characteristic curve, receiver operating characteristic, accuracy, specificity, and F1 score were employed. In the test set, the model showcased an area under the curve (AUC) of 0.968, accuracy of 94.3%, specificity of 88.9%, and an impressive F1 score of 99.0%. 
The systematic review of various architectures and methodologies reveals several key insights and opportunities for future development. The primary contribution of this research lies in the comprehensive evaluation of different deep learning architectures for COVID-19 detection. The comparative analysis of models such as VGG16, VGG19, MobileNetV2, InceptionResNetV2, and others provides valuable insights into their relative strengths and limitations. MobileNetV2, in particular, has demonstrated exceptional performance across multiple studies, suggesting its potential as a preferred architecture for resource-constrained deployment scenarios. A significant gap identified in the current research landscape is the limited standardization of evaluation metrics and datasets across studies. While many researchers report high accuracy values, the variation in dataset composition, preprocessing methods, and validation strategies makes direct comparisons challenging. Future research would benefit from establishing standardized benchmarks and evaluation protocols to enable more meaningful comparisons between different approaches. The prevention of overfitting, a critical concern in medical image analysis, has been addressed through various strategies in the reviewed studies. These include data augmentation techniques, dropout layers, and proper validation protocols. However, there is room for improvement in developing more robust regularization techniques specifically tailored to medical imaging applications. 

3.3 Performance of Models in Detecting COVID-19 in Computed Tomography Scans

Concerning the detection of COVID-19 on CT scans, deep learning models can be used to collaborate with other existing processes of detection. Detecting COVID-19 using deep learning on CT scans has been a significant area of research and development. In order to achieve #Objective_1 several studies were analysed and the accuracies compared (see Table 8) concerning the detection of COVID-19 on CT scans, where the previous model of the authors, CTCovid (Antunes et al., 2024) displayed the highest results. 

Table 7. Studies using deep learning to detect COVID-19 on CT scans and the results obtained.
Study	Method	Results
(Yasar & Ceylan, 2020)
23-layer deep CNN	Accuracy = 95.9%
(Han et al., 2020)
C3D, DeCoVNet and
AD3D-MIL Algorithm	Accuracy = 96,8%
(Ardakani et al., 2020)
Pre-processing (Cropped / Input Image Size: 60x60) and Transfer Learning with Convolutional Neural Networks (AlexNet, VGG-16,
VGG-19, SqueezeNet, GoogleNet,
MobileNet-V2, ResNet-18,
ResNet-50, ResNet-101, and
Xception)	Accuracy = 78,92%
(Amyar et al., 2020)
Multitask DL (with the encoder and the decoder)	Accuracy = 94.6%
(Wang et al., 2020)
3D-ResNets 	Accuracy = 93.3%
(Jaiswal et al., 2020)
Transfer Learning with Convolutional Neural Networks (VGG16, Inception ResNet, ResNet 152V2,
DenseNet201)	Accuracy = 90.9%
(Sun et al., 2020)
AFS-DF 	Accuracy = 91.7%
(Pathak et al., 2022)
Transfer Learning with Convolutional Neural Networks (Transfer
from ResNet-50 Network to a New
CNN Architecture)	Accuracy = 93.02%
(Hasan et al., 2021)
DenseNet-121	Accuracy = 92.0%
(Ouyang et al., 2020)
Convolutional Neural Network (3D ResNet34) and Uniform Sampling.	Accuracy = 87,5%
(Antunes et al., 2024)
CTCovid	Accuracy = 99.8%

The CTCovid19 model (Antunes et al., 2024) is a new approach designed for COVID-19 detection, utilizing a specialized deep learning structure. ResNet-50, trained with ImageNet, forms the base of this model. To improve its ability to identify COVID-19 patterns in Computed Tomography (CT) scans, the network was fine-tuned by adjusting existing layers and adding new ones. The model demonstrated accuracy rates ranging from 97.0% to 99.8% across three well-known and documented datasets focused on COVID-19 detection.
After reviewing extensive literature on COVID-19 detection using CT scans, several significant research contributions have emerged in this domain. The development of specialized architectures like CTCovid and CovidxNet-CT represents a major advancement, demonstrating the field's evolution toward more targeted solutions. These models have achieved remarkable accuracy rates, with some approaches reaching up to 99.8% accuracy on standardized datasets. The systematic review of papers utilizing CT scan datasets has revealed several notable gaps in current research approaches. One significant gap lies in the limited diversity of datasets used for model validation, with many studies focusing on specific geographic regions or demographic groups. This limitation potentially affects the generalizability of the models across different populations and healthcare settings. Another gap involves the inconsistent reporting of model interpretability measures, with many studies focusing primarily on accuracy metrics while providing limited insight into the decision-making process of their models. The research has highlighted several areas that could be improved to enhance the effectiveness of COVID-19 detection systems. Additionally, the development of more sophisticated data augmentation techniques specifically designed for CT scans could help address the challenge of limited dataset sizes while maintaining the specific characteristics of COVID-19 manifestations in imaging. To prevent overfitting, several strategies have emerged as particularly effective in the context of CT scan analysis. The implementation of progressive learning approaches, where models are trained on increasingly complex features, has shown promise in developing more robust solutions. 

3.4 Results Concerning Automated Detection of Pneumonia in X-ray Images

Advanced artificial intelligence models have demonstrated remarkable accuracy in identifying pneumonia through chest X-ray analysis. Recent peer-reviewed studies show these automated systems achieving both sensitivity and specificity rates exceeding 90%. 
In order to achieve #Objective_2, several studies were analysed ( see Table 9) comparing the results obtained from different studies concerning the use of deep learning to detect Pneumonia on X-rays.


Table 8. Studies using deep learning to detect pneumonia on X-rays and the results obtained.
Study	Method	Results
(Li et al., 2021)
VGG-16	Accuracy = 93.57%
(Ibrahim et al., 2021)
AlexNet	Accuracy = 93.42%
(Varshni et al., 2019)
AlexNet, GoogLeNet
and ResNet	Accuracy = 90.7%
(Chouhan et al., 2020)
VGG-16	Accuracy = 93.0%
(Hammoudi et al., 2021)
InceptionResNetV2	Accuracy = 90.7%
(Sitaula & Hossain, 2020)
Attention-based
VGG-16	Accuracy = 87.49%
(Szepesi & Szilágyi, 2022)
CNN + modified
dropout Model	Accuracy = 91.0%
(Al-Taani & Al-Dagamseh, 2022)
Pre-activation ResNet
with DenseNet169	Accuracy = 90%
(Reshan et al., 2023)
MobileNet	Accuracy = 94.23%

The application of artificial intelligence to pneumonia detection in X-ray imaging has emerged as a significant advancement in medical diagnostics. In the  analysis of (Reshan et al., 2023) a deep learning model is showcased to distinguish between normal and severe pneumonia cases. The entire proposed system comprises eight pre-trained models: ResNet50, ResNet152V2, DenseNet121, DenseNet201, Xception, VGG16, EfficientNet, and MobileNet. These models were tested on two datasets containing 5856 and 112,120 chest X-ray images. The MobileNet model achieves the highest accuracy, scoring 94.23% and 93.75% on the respective datasets. Various crucial hyperparameters such as batch sizes, epochs, and different optimizers were carefully considered when comparing these models to identify the most suitable one. To distinguish pneumonia cases from normal instances, the capabilities of five pre-trained CNN models namely ResNet50, ResNet152V2, DenseNet121, DenseNet201, and MobileNet have been assessed. The most favourable outcome is achieved by MobileNet using 16 batch sizes, 64 epochs, and the ADAM optimizer. Validation of predictions has been conducted on publicly accessible chest radiographs. The MobileNet model exhibits an accuracy of 94.23%. 
The comprehensive review has revealed that transfer learning approaches, particularly those utilizing pre-trained models like VGG16, ResNet, and MobileNet, have demonstrated remarkable effectiveness in pneumonia detection. Through careful examination of the literature, several notable gaps have emerged in current research approaches. A primary gap exists in the limited exploration of model interpretability, particularly in explaining the decision-making process in clinical contexts. Another significant gap involves the insufficient standardization of preprocessing techniques across different studies, making direct comparisons of model performances challenging. The variation in dataset compositions and evaluation metrics also presents a barrier to comprehensive comparative analysis. The research landscape could be improved through several targeted approaches. To address the critical issue of overfitting, several effective strategies have emerged from the reviewed studies. The implementation of modified dropout techniques, as demonstrated in recent research, has shown promise in improving model generalization. Careful attention to validation protocols, including the use of diverse datasets from multiple institutions, helps ensure model robustness
This systematic review has made several key contributions to the field. It has provided a comprehensive analysis of current approaches, identified critical gaps in existing research, and suggested practical directions for future development. 

3.5 Analysis of Web-Based Systems for Detecting COVID-19 and Pneumonia

A web Chest X-ray Classification tool was built in the work of (Nandagobalan, & Chaw, 2023) using Python and Streamlit to detect COVID-19 infections from chest X-ray images, as well as other conditions like Bacterial and Viral Pneumonia. Users can upload an X-ray image using the "Upload File" option to receive the diagnostic results as shown on Figure 11.
 
Figure 11. Interface of the application developed by (Nandagobalan, & Chaw, 2023).

Concerning the research of (Islam et al., 2024) an app was developed using Flask, which allows users to submit image inputs, and the model then returns its predictions based on those images.
The work of (Antunes et al., 2024) shows an innovative approach that advocates the use of patient files and XAI. A web-based diagnostic application is introduced to assist physicians in the diagnostic process. It uses a modified deep neural network (AlexNet) to detect COVID-19 in X-rays and CT scans, as well as pneumonia in X-rays. The system achieved accuracy rates exceeding 90% across seven well-known and documented datasets related to COVID-19 and pneumonia detection in X-rays and COVID-19 detection in CT scans. The web application, illustrated in Figure 12, was developed using PHP alongside a MySQL server database, providing a versatile platform for medical imaging analysis. It includes a user-friendly uploader for X-ray and CT scan submissions. Once an image is uploaded, the system uses a deep learning model built with Python Flask, to detect COVID-19 in both X-rays and CT scans, as well as pneumonia in X-rays. Figure 12 shows two views of the AI Health interface. Several APIs were integrated into the controller layer to ensure seamless communication across different parts of the application. These APIs handle tasks such as image uploads, initiating the deep learning analysis, and retrieving and displaying the results in the web interface.
 
Figure 12. Block diagram of the web diagnosis application developed by (Antunes et al., 2024).

In order to achieve #Objective_3 the research led to an improvement of the previous applications  developed by the authors where a video chat was implemented plus XAI strategies to handle image data, and use of a VLM and LLM to generate the medical report (see Figure 13) (source code at: kucaantunes/XaiMed--A-web-App-that-uses-XAI-LLMs-VLM-to-generate-medical-reports), several preprocessing functions are defined. One function resizes the input images to a standard size and normalizes pixel values to optimize performance in deep learning models. Another function uses a chest X-ray verification model to assess whether the uploaded image is indeed a chest X-ray, providing a probability value.
The core of the model’s interpretability is Grad-CAM, a technique used to generate heatmaps that highlight the regions of an image most relevant to the model’s decision. The app contains a function that computes this heatmap by evaluating gradients and activations from the model's layers. Another key function converts images into Base64 format for easy transmission over the web. This allows the app to send images as strings in JSON responses, which is essential for web-based applications.
The main prediction route processes uploaded images and uses the transformer-based model to extract features, which are then classified. A Grad-CAM visualization is generated, and all results, including predictions and images, are returned as a JSON response with Base64-encoded images.
Additionally, there is a route for serving random example images, offering users a way to view sample images from a predefined directory. 
 
 
 
Figure 13. Improvements on the previously developed application (Antunes, et al. 2024) adapted from  (Pitumbur, 2023).
Algorithm 4, begins by initializing a Flask application to handle HTTP requests. It loads two pre-trained models: CLIP for image classification and GPT-Neo for the generation of detailed medical reports. Upon receiving a GET request, the home template is rendered. If a POST request is received, the input image undergoes preprocessing, including resizing and normalization. If the input image is recognized as a chest X-ray, the CLIP model is used to classify the image into one of three categories: Normal, COVID-19, or Pneumonia. Subsequently, the algorithm generates a Grad-CAM heatmap to highlight regions within the image that contribute significantly to the model's decision. Once the image is successfully loaded and pre-processed, convolutional neural network (CNN) features are extracted, flattened, and passed through the classification model to generate a prediction. A comprehensive clinical report is then generated using GPT-Neo, contextualized by the classification output. The Grad-CAM heatmap is superimposed onto the original image, providing a visual representation of the model’s decision-making process. The original image, heatmap, and superimposed image are converted to Base64 format to facilitate seamless transmission. The response includes the predicted class, associated probability, a detailed medical report, and visualizations. 
Algorithm 4: Chest X-ray Image Classification and Grad-CAM Visualization

Input:
An image file via POST request.
Output:
Predicted class.
Prediction probability.
Medical report. 
Chest X-ray probability and visualizations (original image, heatmap, and superimposed image).
Steps:
Initialize Flask app.
Load pre-trained model CLIP for image classification.
Load pre-trained model GPT-Neo for report generation.
Render home template for GET request.
if request is POST then
   Render error message.
End If
Preprocess input image (resize and normalize).
If image is chest X-ray, then
   Predict the class using the pre-trained CLIP model (Normal, COVID-19, or Pneumonia).
End If
Generate Grad-CAM heatmap.
If request is missing file, then
   return 400 Bad Request.
End If
Load and preprocess image for prediction.
Extract features from image using CNN model.
Flatten CNN features.
Predict class.
Generate a detailed clinical report using GPT-Neo based on the classification results.
Generate Grad-CAM heatmap for visualization by extracting features from the image using the CLIP model.
Superimpose heatmap on original image.
Convert original image, heatmap, and superimposed image to Base64.
Return prediction results and images in response.
If error occurs, then
   return 500 Internal Server Error.
End If


4. Conclusions, Limitations and Future Research

The research in cause proposes an innovative process of performing systematic literature reviews and several processes on how to detect diseases from medical images, improving the traditional processes of online diagnosis. The algorithms analysed allow to perform several functionalities and providing an innovative concept that can be helpful for detecting diseases. The development process was described, and tests were performed to validate the proposed solutions. The research took in consideration several sources of information and many articles of other researchers. In some cases, it was possible to obtain a high accuracy. The presented solution consists in an integrator of several analysed researches that complement traditional processes. The work required extensive research and several mechanisms were used to achieve the desired results. An innovative approach was demonstrated that allows to facilitate the process of generating systematic literature reviews. The proposed solution basis on a new concept of e-health systems that contrarily to traditional processes allows to give prediction to the doctor about the existence of a specific disease after uploading a medical image using XAI, VLM and LLM.

4.1 Answers to the Research Questions

Following the analysis, conclusions were drawn, and a series of applications were created to meet the objectives and address the research questions posed in the study. The developed solutions provided clear answers to the investigation's key queries.
How to improve the performance of the current detection processes of COVID-19 based in an X-ray or CT scan using deep learning (#Research_Question_1)?
Concerning the detection of COVID on CT scans, several studies mentioned high accuracy results like in (Antunes et al., 2024) with rates that went from 97.0% to 99.8% across three widely recognized and documented datasets dedicated to COVID-19 detection. The research of (Han et al., 2020) also shown high accuracy results around 96.8%. For the detection of COVID on X-rays the study of (Minaee et al., 2020) showed a Sensitivity of 98%, and a Specificity of 92.9% and the research of (Ucar, & Korkmaz, 2020) an accuracy of 98.26%.
To enhance the performance of COVID-19 detection based on X-ray and CT scans through deep learning, several strategies can be employed like increasing the size of the training dataset and ensuring that it includes high-quality, diverse images from multiple sources that can significantly improve model performance. Incorporating images that capture a wide range of disease presentations helps the model generalize better, also the use of more advanced deep learning architectures, such as fine-tuned pre-trained models (on example, ResNet, DenseNet, or EfficientNet), or hybrid models that combine convolutional neural networks (CNNs) with attention mechanisms, can lead to better accuracy in detecting abnormalities in medical images. Enhancing the dataset with techniques like image augmentation (flipping, rotating, scaling) can help the model learn invariant features and improve its robustness. Preprocessing steps like noise reduction, contrast enhancement, and lung region segmentation also refine image quality before analysis. Combining predictions from multiple models using ensemble techniques such as bagging or boosting can increase detection accuracy by reducing individual model bias and variance. Leveraging models pre-trained on large-scale medical datasets can speed up the learning process and improve detection results, particularly when the available COVID-19 dataset is limited. Continuously updating the model with new data, including images of emerging variants of COVID-19, can improve detection reliability over time. Enhancing model performance by incorporating additional patient data (age, medical history, symptoms) alongside imaging can provide a more comprehensive diagnostic tool and improve the accuracy of COVID-19 detection.
By adopting these techniques, deep learning models can offer faster, more accurate, and reliable COVID-19 diagnoses from X-ray and CT scan images.
Which public datasets can be used in order to improve the accuracy of the prediction (#Research_Question_2)?
Numerous publicly available datasets exist for detecting COVID-19 and pneumonia. To enhance the accuracy of predictions in deep learning models, particularly for detecting COVID-19 using X-rays and CT scans, careful dataset preparation and treatment are essential. The dataset should be clean by eliminating poor-quality or irrelevant images that may mislead the model. Normalizing pixel values to a standard range (example given, 0 to 1 or -1 to 1), ensuring uniformity in input data, helps the model converge more efficiently. Resizing all images to a consistent dimension, so the model can process them uniformly without losing key features. Techniques like rotation, flipping, zooming, and cropping help to artificially expand the dataset. This creates more diverse image representations and helps the model generalize better. Controlled noise or blurring can improve robustness by forcing the model to focus on key features rather than superficial details. If there is an imbalance between the number of positive and negative cases, using techniques like oversampling the minority class, under sampling the majority class, or applying Synthetic Minority Over-sampling Technique (SMOTE) allows to create a more balanced dataset. The training, validation, and testing sets maintain the same ratio of positive and negative cases to avoid biased learning. In medical imaging, segmenting the lungs or relevant areas can help the model focus on critical regions, reducing the noise from irrelevant parts of the image. Applying lung segmentation masks to isolate the areas most affected by diseases, like COVID-19, ensuring that the model learns from the correct regions. Accurate and consistent labelling of images is crucial. Mislabelling can confuse the model, reducing accuracy. For conditions like pneumonia and COVID-19, multi-label classification can be used to account for patients who may have both conditions. By properly preparing and treating datasets, deep learning models can be trained more effectively, leading to improved prediction accuracy for COVID-19 and other medical conditions.
How can pneumonia be detected via deep learning (#Research_Question_3)?
Pneumonia detection through deep learning leverages advanced algorithms to analyse medical imaging data, particularly chest X-rays and CT scans. The process begins with data collection, where a robust dataset of high-quality images is gathered, often from publicly available resources containing labelled cases of pneumonia. Accurate labelling is crucial, as it directly impacts the model's training efficacy.
The research of (Reshan et al., 2023) using the MobileNet showed an Accuracy of 94.23% and the research of (Antunes et al., 2024) reached and accuracy of 98.9% by using a modified version of AlexNet.
Once the dataset is acquired, preprocessing is essential. This involves enhancing image quality through normalization, resizing, and denoising to ensure consistency. Data augmentation techniques, such as rotation, flipping, and zooming, are employed to artificially expand the dataset, introducing variability that helps the model generalize better.
Selecting an appropriate deep learning architecture is vital for effective pneumonia detection. CNNs are commonly used due to their ability to automatically extract relevant features from images. Popular architectures include ResNet, DenseNet, and VGGNet, which are tailored for image classification tasks.
Training the model involves dividing the dataset into training, validation, and test sets. The model learns to recognize pneumonia-related patterns by adjusting its parameters to minimize prediction errors during this phase. Transfer learning can also be applied, utilizing pre-trained models to accelerate training and improve accuracy by leveraging knowledge from large-scale datasets. After training, the model is evaluated on a separate test set to assess its performance, using metrics like accuracy, precision, recall, and F1-score. A high recall rate is particularly critical, as it indicates the model's effectiveness in correctly identifying pneumonia cases. Once trained and evaluated, the model can predict pneumonia in new images, providing rapid feedback to healthcare professionals. Visualization techniques, such as Grad-CAM, can enhance interpretability by highlighting which areas of an image influenced the model's predictions, building trust in AI-assisted diagnostics. Overall, deep learning has the potential to significantly improve pneumonia detection by automating the analysis of medical images, enabling faster and more accurate diagnoses, and ultimately enhancing patient care.
How can web applications be developed in order to facilitate the diagnosis process and to ameliorate the explanations of the CNN previsions using explainable artificial intelligence (#Research_Question_4)?
Developing web applications to facilitate the diagnosis process and improve the explanations of Convolutional Neural Network (CNN) predictions using explainable artificial intelligence (XAI) requires a thoughtful approach that prioritizes usability, integration of advanced AI techniques, and adherence to security standards. To start, a user-friendly interface is essential. Healthcare professionals should be able to easily upload medical images, such as X-rays or CT scans, without encountering technical hurdles. This can be achieved by providing straightforward file upload options and a clear result dashboard that displays predictions, confidence levels, and relevant metrics. Ensuring the interface is intuitive and accessible will enhance user engagement and facilitate quicker adoption. On the backend, selecting a robust framework like Flask or Django allows for efficient handling of requests and management of server-side logic. The trained CNN model must be seamlessly integrated into this backend, enabling it to process incoming images and generate predictions in real time. This requires careful optimization to ensure fast response times, which is crucial in a clinical setting. The researches of  (Nandagobalan, & Chaw, 2023), (Islam et al., 2024) and (Antunes et al., 2024) show a possibility of detecting pulmonary diseases online. Incorporating explainable AI techniques is vital for enhancing the interpretability of CNN predictions. Tools such as Grad-CAM can generate saliency maps that highlight the regions of the image that influenced the model's decisions, helping users understand which features are significant in the diagnosis. Other methods, like LIME  and shapley additive explanations (SHAP), can further clarify how various aspects of an image contribute to the final predictions, providing valuable insights that empower healthcare providers to make informed decisions. Displaying performance metrics, including accuracy, precision, recall, and F1-score, in the results section adds another layer of trustworthiness to the application. These metrics help users gauge the reliability of the predictions, reinforcing their confidence in the system.
A feedback mechanism is also crucial; allowing healthcare professionals to report errors or provide insights on the predictions can create a feedback loop that continually enhances the model's performance and the application’s usability. This iterative improvement process is key to developing a system that adapts to the evolving landscape of medical diagnoses. Data security must not be overlooked. The application should comply with healthcare regulations to protect sensitive patient information. Implementing secure data transmission, user authentication, and encryption practices ensures that privacy and security are maintained throughout the diagnostic process. To keep the model relevant and accurate, integrating a continuous learning mechanism is beneficial. This allows the model to be updated with new data over time, helping it adapt to emerging trends and new variants of diseases.
The use of VLMs and LLMs can facilitate the comprehension of the physician by providing AI generated text which describes the process used and answers to any question facilitating the analysis.

4.2 Limitations

While artificial intelligence models have demonstrated impressive accuracy in medical image analysis, several significant limitations and challenges warrant careful consideration. Although prediction accuracies often exceed 90%, there remains substantial room for improvement, particularly in handling edge cases and unusual presentations of diseases. The integration of multiple diagnostic approaches, including laboratory testing, clinical examinations, and various imaging modalities, has shown promising results, suggesting the importance of comprehensive diagnostic frameworks. A critical limitation lies in the quality and consistency of medical imaging data. The varying levels of noise in CT scans and X-rays present significant challenges for automated analysis systems. Image quality can be affected by numerous factors, including equipment variations, acquisition protocols, and patient positioning. These variations necessitate sophisticated preprocessing techniques and robust model architectures capable of handling diverse image qualities. The calibration of model parameters presents another significant challenge. The specificity requirements for different types of medical analyses vary considerably, and models must be carefully tuned to maintain high performance across different diagnostic scenarios. This calibration process requires extensive validation across diverse patient populations and clinical settings to ensure reliable performance.
The current research aims to complement traditional diagnostic processes by providing automated comparison capabilities between uploaded images and comprehensive datasets of both positive and negative cases. However, this approach faces several limitations. The representativeness of training datasets remains a crucial concern, as they may not fully capture the wide spectrum of disease presentations and patient demographics. Additionally, the challenge of dataset bias must be carefully addressed to ensure equitable performance across different patient populations. The occurrence of false positives and false negatives represents a significant challenge in medical image analysis. While model accuracy can be improved through careful hyperparameter optimization and extensive testing, the critical nature of medical diagnosis requires extremely high reliability standards. The impact of false results must be carefully considered in the context of clinical decision-making processes. Furthermore, the integration of automated analysis systems into existing clinical workflows presents substantial challenges. Healthcare providers must carefully balance the benefits of automated analysis with the need for human oversight and interpretation. The complementary nature of artificial intelligence in medical diagnosis must be emphasized, as these systems are designed to support, not replace, clinical expertise. Another significant limitation involves the interpretability of model decisions. While current systems can achieve high accuracy rates, explaining the reasoning behind specific predictions remains challenging. This lack of transparency can impact clinical adoption and trust in automated analysis systems.
The specificity of medical conditions and individual patient circumstances often necessitates additional diagnostic procedures beyond imaging analysis. These may include medical scans, biopsies, or other specialized diagnostic processes. The limitations of imaging-based analysis must be acknowledged, particularly in complex cases where multiple diagnostic approaches may be required. Research challenges also extend to the validation and certification of automated medical image analysis systems. Regulatory requirements and clinical validation standards must be carefully considered in the development and deployment of these systems. The need for extensive clinical trials and validation studies represents a significant barrier to widespread adoption. The dynamic nature of medical knowledge and practice presents additional challenges. Models must be designed with the capability for continuous updating and refinement as new medical knowledge emerges and diagnostic criteria evolve. This requirement for ongoing development and validation adds complexity to the implementation of automated analysis systems. These limitations and challenges underscore the importance of continued research and development in medical image analysis. Future work should focus on addressing these constraints through improved methodologies, more comprehensive validation approaches, and enhanced integration with clinical practice. The goal remains to develop robust, reliable, and clinically valuable tools that can effectively support medical professionals in their diagnostic work.

4.3 Future Investigation

In the future it is expected to develop better and more accurate models, the research will follow a methodology based on using public datasets and compare the results with other researchers on the same datasets. The web application will be improved in order to facilitate the use by the physician. Adding a patient file will facilitate the process of diagnosis and the use of XAI also helps by showing which areas the prediction focused on.
Detecting diseases presents challenges as the process is labour-intensive and time-consuming, heavily reliant on external factors. To minimize human error, emerging artificial intelligence technologies can provide more accurate, cost-effective, and efficient solutions, although they do come with some limitations that can help prevent mistakes made by physicians. This topic opens up numerous areas for further research. Deep learning models and AI algorithms still face challenges related to the classification accuracy of X-rays, CT scans, and MRI scans. Future enhancements to the image uploader could involve incorporating different models for processing image datasets.

4.4 ACKNOWLEDGES

This work was supported by the Portuguese Foundation for Science and Technology (FCT) project NOVA LINCS ref. UIDB/04516/2020 (https://doi.org/10.54499/UIDB/04516/2020) and ref. UIDP/04516/2020 (https://doi.org/10.54499/UIDP/04516/2020) with the financial support of FCT.IP, and by FCT project ALGORITMI (UIDB/00319/2020). 


References
Abbas, A., Abdelsamea, M. M., & Gaber, M. M. (2020). Classification of COVID-19 in chest X-ray images using DeTraC deep convolutional neural network. In Applied Intelligence (Vol. 51, Issue 2, pp. 854–864). Springer Science and Business Media LLC. https://doi.org/10.1007/s10489-020-01829-7.
Acharya, D., Park, J., Lee, Y., Hamm, I. S., Lee, D. S., Moon, S.-S., & Lee, K. (2020). Clinical Characteristics of the COVID-19 Patients with Pneumonia Detected by Computerized Tomography but Negative for Infiltration by X-ray. In Healthcare (Vol. 8, Issue 4, p. 518). MDPI AG. https://doi.org/10.3390/healthcare8040518.
Afshar, P., Heidarian, S., Naderkhani, F., Oikonomou, A., Plataniotis, K. N., & Mohammadi, A. (2020). Covid-CAPS: A capsule network-based framework for identification of COVID-19 cases from X-ray images. In Pattern Recognition Letters (Vol. 138, pp. 638–643). Elsevier BV. https://doi.org/10.1016/j.patrec.2020.09.010.
Ahmad, I. S., Li, N., Wang, T., Liu, X., Dai, J., Chan, Y., Liu, H., Zhu, J., Kong, W., Lu, Z., Xie, Y., & Liang, X. (2023). COVID-19 Detection via Ultra-Low-Dose X-ray Images Enabled by Deep Learning. In Bioengineering (Vol. 10, Issue 11, p. 1314). MDPI AG. https://doi.org/10.3390/bioengineering10111314.
Ahsan, M. M., Gupta, K. D., Islam, M. M., Sen, S., Rahman, M. L., & Shakhawat Hossain, M. (2020). COVID-19 symptoms detection based on nasnetmobile with explainable ai using various imaging modalities. Machine Learning and Knowledge Extraction, 2(4), 490-504. https://doi.org/10.3390/make2040027.
Alam, K., & Akter, R. Covid 19 And General Pneumonia detection from X Ray image using Deep Learning Approach. https://vixra.org/pdf/1906.0056v1.pdf.
Alharbi, A. H., & Hosni Mahmoud, H. A. (2022). Pneumonia Transfer Learning Deep Learning Model from Segmented X-rays. In Healthcare (Vol. 10, Issue 6, p. 987). MDPI AG. https://doi.org/10.3390/healthcare10060987.
Ali, W., Qureshi, E., Farooqi, O. A., & Khan, R. A. (2023). Pneumonia Detection in Chest X-Ray Images: Handling Class Imbalance (Version 1). arXiv. https://doi.org/10.48550/ARXIV.2301.08479.

Al-Madani, A. M., Gaikwad, A. T., Ahmed, Z. A. T., Mahale, V., Alsubari, S. N., & Tawfik, M. (2022). Web Application Based on Deep Learning for Detecting COVID-19 Using Chest X-Ray Images. In TELe-Health (pp. 283–294). Springer International Publishing. https://doi.org/10.1007/978-3-030-99457-0_18.
Al-Taani, A. T., & Al-Dagamseh, I. T. (2022). Automatic Detection of Pneumonia using Concatenated Convolutional Neural Network. Research Square Platform LLC. https://doi.org/10.21203/rs.3.rs-2220817/v1.
Angelov, P., & Soares, E. (2020). Explainable-by-Design Approach for COVID-19 Classification via CT-scan. Cold Spring Harbor Laboratory. https://doi.org/10.1101/2020.04.24.20078584.
Antunes, C. (2021). Microsoft power BI. Retrieved February 5, 2023, from https://app.powerbi.com/view?r=eyJrIjoiZDQ3YWI2ZWMtZTJiOC00MTk3LTlkM2UtMTZhMjZlMzkzYjdjIiwidCI6ImY2MTBjMGI3LWJkMjQtNGIzOS04MTBiLTNkYzI4MGFmYjU5MCIsImMiOjh9.
Antunes, C., & Coutinho, C. (2022). Employment of Artificial Intelligence Mechanisms for e-Health Systems in Order to Obtain Vital Signs Improving the Processes of Online Consultations and Diagnosis. In 2022 International Symposium on Sensing and Instrumentation in 5G and IoT Era (ISSI). 2022 International Symposium on Sensing and Instrumentation in 5G and IoT Era (ISSI). IEEE. https://doi.org/10.1109/issi55442.2022.9963223.
Antunes, C., Rodrigues, João M.F., & Cunha, A. (2024). Web Diagnosis for COVID-19 and Pneumonia Based on Computed Tomography Scans and X-rays, Accepted to 18th International Conference on Universal Access in Human-Computer Interaction, part of HCI International 2024, 29 June - 4 July 2024, Washington DC, USA. https://doi.org/10.1007/978-3-031-60884-1_14.
Antunes, C., Rodrigues, J., & Cunha, A. (2025). CTCovid19: Automatic COVID-19 model for Computed Tomography Scans Using Deep Learning. In Intelligence-Based Medicine (Vol. 11, p. 100190). Elsevier BV. https://doi.org/10.1016/j.ibmed.2024.100190.
Apostolopoulos, I. D., & Mpesiana, T. A. (2020). COVID-19: automatic detection from X-ray images utilizing transfer learning with convolutional neural networks. In Physical and Engineering Sciences in Medicine (Vol. 43, Issue 2, pp. 635–640). Springer Science and Business Media LLC. https://doi.org/10.1007/s13246-020-00865-4.
Ardakani, A. A., Kanafi, A. R., Acharya, U. R., Khadem, N., & Mohammadi, A. (2020). Application of deep learning technique to manage COVID-19 in routine clinical practice using CT images: Results of 10 convolutional neural networks. In Computers in Biology and Medicine (Vol. 121, p. 103795). Elsevier BV. https://doi.org/10.1016/j.compbiomed.2020.103795.
Aresta, G., Jacobs, C., Araújo, T., Cunha, A., Ramos, I., van Ginneken, B., & Campilho, A. (2019). iW-Net: an automatic and minimalistic interactive lung nodule segmentation deep network. Scientific reports, 9(1), 1-9. https://doi.org/10.48550/arXiv.1811.12789.
Aria, M. (2021, January 24). COVID-19 lung CT scans. Kaggle. Retrieved February 5, 2023, from https://www.kaggle.com/datasets/mehradaria/Covid19-lung-ct-scans.
Arias-Londono, J. D., Gomez-Garcia, J. A., Moro-Velazquez, L., & Godino-Llorente, J. I. (2020). Artificial Intelligence Applied to Chest X-Ray Images for the Automatic Detection of COVID-19. A Thoughtful Evaluation Approach. In IEEE Access (Vol. 8, pp. 226811–226827). Institute of Electrical and Electronics Engineers (IEEE). https://doi.org/10.1109/access.2020.3044858.
Asefi, H., & Safaie, A. (2020). The Role of Chest CT Scan in Diagnosis of COVID-19 [JD]. Advanced Journal of Emergency Medicine, 4(2s). https://doi.org/10.22114/ajem.v4i2s.451.
Ayalew, A. M., Salau, A. O., Tamyalew, Y., Abeje, B. T., & Woreta, N. (2023). X-Ray image-based COVID-19 detection using deep learning. In Multimedia Tools and Applications (Vol. 82, Issue 28, pp. 44507–44525). Springer Science and Business Media LLC. https://doi.org/10.1007/s11042-023-15389-8.
Ayanso, A., Lertwachara, K., & Vachon, F. (2011). Design and Behavioral Science Research in Premier IS Journals: Evidence from Database Management Research. 138-152.  https://doi.org/10.1007/978-3-642-20633-7_10.
Babukarthik, R. G., Adiga, V. A. K., Sambasivam, G., Chandramohan, D., & Amudhavel, J. (2020). Prediction of COVID-19 Using Genetic Deep Learning Convolutional Neural Network (GDCNN). In IEEE Access (Vol. 8, pp. 177647–177666). Institute of Electrical and Electronics Engineers (IEEE). https://doi.org/10.1109/access.2020.3025164.
Bargshady, G., Zhou, X., Barua, P. D., Gururajan, R., Li, Y., & Acharya, U. R. (2022). Application of CycleGAN and transfer learning techniques for automated detection of COVID-19 using X-ray images. In Pattern Recognition Letters (Vol. 153, pp. 67–74). Elsevier BV. https://doi.org/10.1016/j.patrec.2021.11.020.
Blanche, L. (2020, April 9). COVID-19 lung CT scans. Kaggle. Retrieved February 5, 2023, from https://www.kaggle.com/datasets/luisblanche/Covidct?select=CT_NonCovid.
Brima, Y., Atemkeng, M., Tankio Djiokap, S., Ebiele, J., & Tchakounté, F. (2021). Transfer Learning for the Detection and Diagnosis of Types of Pneumonia including Pneumonia Induced by COVID-19 from Chest X-ray Images. In Diagnostics (Vol. 11, Issue 8, p. 1480). MDPI AG. https://doi.org/10.3390/diagnostics11081480.
Canayaz, M., Şehribanoğlu, S., Özdağ, R., & Demir, M. (2022). COVID-19 diagnosis on CT images with Bayes optimization-based deep neural networks and machine learning algorithms. In Neural Computing and Applications (Vol. 34, Issue 7, pp. 5349–5365). Springer Science and Business Media LLC. https://doi.org/10.1007/s00521-022-07052-4.
Cellina, M., Martinenghi, C., Marino, P., & Oliva, G. (2021). COVID-19 pneumonia—ultrasound, radiographic, and computed tomography findings: a comprehensive pictorial essay. In Emergency Radiology. Springer Science and Business Media LLC. https://doi.org/10.1007/s10140-021-01905-6.
Chandra, T. B., Verma, K., Singh, B. K., Jain, D., & Netam, S. S. (2021). Coronavirus disease (COVID-19) detection in Chest X-Ray images using majority voting based classifier ensemble. In Expert Systems with Applications (Vol. 165, p. 113909). Elsevier BV. https://doi.org/10.1016/j.eswa.2020.113909.
Chimote, G., & Karandikar, A. M. (2022). COVID-19 pneumonia detection using chest X-ray processing. In International journal of health sciences (pp. 10546–10560). Universidad Tecnica de Manabi. https://doi.org/10.53730/ijhs.v6ns1.7541.
Choomueang, W., Withoonchatri, C., Janwong, P., & Sa-Ing, V. (2023). CCVNet: COVID-19 Detection in Chest X-ray Imaging based on Convolutional Neural Network. In 2023 the 7th International Conference on Medical and Health Informatics (ICMHI). ICMHI 2023: 2023 the 7th International Conference on Medical and Health Informatics. ACM. https://doi.org/10.1145/3608298.3608299.
Chouat, I., Echtioui, A., Khemakhem, R., Zouch, W., Ghorbel, M., & Hamida, A. B. (2022). COVID-19 detection in CT and CXR images using deep learning models. Biogerontology, 23(1), 65–84. https://doi.org/10.1007/s10522-021-09946-7.
Chouhan, V., Singh, S. K., Khamparia, A., Gupta, D., Tiwari, P., Moreira, C., Damaševičius, R., & de Albuquerque, V. H. C. (2020). A Novel Transfer Learning Based Approach for Pneumonia Detection in Chest X-ray Images. In Applied Sciences (Vol. 10, Issue 2, p. 559). MDPI AG. https://doi.org/10.3390/app10020559.
Coenen, M., & Rottensteiner, F. (2019). Probabilistic vehicle reconstruction using a multi-task cnn. Proceedings of the IEEE/CVF International Conference on Computer Vision Workshops. https://doi.org/10.1109/ICCVW.2019.00110.
Dağlarli, E. (2020). Explainable artificial intelligence (xAI) approaches and deep meta-learning models. Advances and applications in deep learning, 79.
Dahmane, O., Khelifi, M., Beladgham, M., & Kadri, I. (2021). Pneumonia detection based on transfer learning and a combination of VGG19 and a CNN Built from scratch. In Indonesian Journal of Electrical Engineering and Computer Science (Vol. 24, Issue 3, p. 1469). Institute of Advanced Engineering and Science. https://doi.org/10.11591/ijeecs.v24.i3.pp1469-1480.
Dandachi, D., & Rodriguez-Barradas, M. C. (2018). Viral Pneumonia: Etiologies and Treatment. In Journal of Investigative Medicine (Vol. 66, Issue 6, pp. 957–965). SAGE Publications. https://doi.org/10.1136/jim-2018-000712.
Dhivya, N., & Sharmila, P. (2023). Multimodal Feature and Transfer Learning in Deep Ensemble Model for Lung Disease Prediction. Journal of Data Acquisition and Processing, 38(2), 271. ISSN: 1004-9037.
Echtioui, A., Zouch, W., Ghorbel, M., Mhiri, C., & Hamam, H. (2020). Detection Methods of COVID-19. SLAS Technology Translating Life Sciences Innovation. 25. 1-7. https://doi.org/10.1177/2472630320962002.
El-Shafai, W. (2020). Extensive COVID-19 X-Ray and CT Chest Images Dataset [dataset]. Mendeley. https://doi.org/10.17632/8H65YWD2JR.3.
El-Shafai, W., A. Mahmoud, A., M. El-Rabaie, E.-S., E. Taha, T., F. Zahran, O., S. El-Fishawy, A., Abd-Elnaby, M., & E. Abd El-Samie, F. (2022). Efficient Deep CNN Model for COVID-19 Classification. In Computers, Materials &amp; Continua (Vol. 70, Issue 3, pp. 4373–4391). Computers, Materials and Continua (Tech Science Press). https://doi.org/10.32604/cmc.2022.019354.
Elkamouny, M., & Ghantous, M. (2022). Pneumonia Classification for COVID-19 Based on Machine Learning. In 2022 2nd International Mobile, Intelligent, and Ubiquitous Computing Conference (MIUCC). 2022 2nd International Mobile, Intelligent, and Ubiquitous Computing Conference (MIUCC). IEEE. https://doi.org/10.1109/miucc55081.2022.9781796.
Elpeltagy, M., & Sallam, H. (2021). Automatic prediction of Covid− 19 from chest images using modified ResNet50. In Multimedia Tools and Applications (Vol. 80, Issue 17, pp. 26451–26463). Springer Science and Business Media LLC. https://doi.org/10.1007/s11042-021-10783-6.
Elshawi, R., Al-Mallah, M. H., & Sakr, S. (2019). On the interpretability of machine learning-based model for predicting hypertension. BMC medical informatics and decision making, 19(1), 1-32.
Elyan, E., Vuttipittayamongkol, P., Johnston, P., Martin, K., McPherson, K., Moreno-García, C. F., Jayne, C., & Mostafa Kamal Sarker, Md. (2022). Computer vision and machine learning for medical image analysis: recent advances, challenges, and way forward. In Artificial Intelligence Surgery. OAE Publishing Inc. https://doi.org/10.20517/ais.2021.15.
Emin Sahin, M. (2022). Deep learning-based approach for detecting COVID-19 in chest X-rays. In Biomedical Signal Processing and Control (Vol. 78, p. 103977). Elsevier BV. https://doi.org/10.1016/j.bspc.2022.103977.
Farooq, M., & Hafeez, A. (2020). Covid-ResNet: A Deep Learning Framework for Screening of Covid19 from Radiographs (Version 1). arXiv. https://doi.org/10.48550/ARXIV.2003.14395.
Fayemiwo, M., Olowookere, T., Arekete, S., Ogunde, A., Odim, M., Oguntunde, B., Olaniyan, O., Ojewumi, T., Oyetade, I., Aremu, A., & Kayode, A. (2021). Modeling a deep transfer learning framework for the classification of COVID-19 radiology dataset. PeerJ. Computer science, 7, e614. https://doi.org/10.7717/peerj-cs.614.
Foysal, Md., Hossain, A. B. M. A., Yassine, A., & Hossain, M. S. (2023). Detection of COVID-19 Case from Chest CT Images Using Deformable Deep Convolutional Neural Network. In H. Lv (Ed.), Journal of Healthcare Engineering (Vol. 2023, pp. 1–12). Hindawi Limited. https://doi.org/10.1155/2023/4301745.
Futia, G., & Vetrò, A. (2020). On the integration of knowledge graphs into deep learning models for a more comprehensible AI—Three challenges for future research. Information, 11(2), 122.
Garcés, M., Rico, S., Cortez-Quiroga, G., Calvo, J., & Guadalquivir, A. (2020). Covid 19. Pathophysiology and prospects for early detection in patients with mild symptoms of the controversial virus in underdeveloped countries: An update on the state. Journal of Health Science and Prevention. https://doi.org/10.13140/RG.2.2.29110.24647.
Ghaderzadeh, M., Asadi, F., Jafari, R., Bashash, D., Abolghasemi, H., & Aria, M. (2021). Deep Convolutional Neural Network–Based Computer-Aided Detection System for COVID-19 Using Multiple Lung Scans: Design and Implementation Study. In Journal of Medical Internet Research (Vol. 23, Issue 4, p. e27468). JMIR Publications Inc. https://doi.org/10.2196/27468.
Ghose, P., Alavi, M., Tabassum, M., Ashraf Uddin, Md., Biswas, M., Mahbub, K., Gaur, L., Mallik, S., & Zhao, Z. (2022). Detecting COVID-19 infection status from chest X-ray and CT scan via single transfer learning-driven approach. In Frontiers in Genetics (Vol. 13). Frontiers Media SA. https://doi.org/10.3389/fgene.2022.980338.
Graham, F. (2021). Daily briefing: How SARS-CoV-2 infects cells. Nature.com. Retrieved 16 June 2022, from https://www.nature.com/articles/d41586-021-02084-7.
Hall, L. O., Paul, R., Goldgof, D. B., & Goldgof, G. M. (2020). Finding COVID-19 from Chest X-rays using Deep Learning on a Small Dataset (Version 4). arXiv. https://doi.org/10.48550/ARXIV.2004.02060.
Hamad, Q., Samma, H., Suandi, S., & Saleh, J. (2022). Study of VGG-19 Depth in Transfer Learning for COVID-19 X-Ray Image Classification. Proceedings of the 11th International Conference on Robotics, Vision, Signal Processing and Power Applications. Lecture Notes in Electrical Engineering, vol 829. Springer, Singapore. https://doi.org/10.1007/978-981-16-8129-5_142.
Hammoudi, K., Benhabiles, H., Melkemi, M., Dornaika, F., Arganda-Carreras, I., Collard, D., & Scherpereel, A. (2021). Deep Learning on Chest X-ray Images to Detect and Evaluate Pneumonia Cases at the Era of COVID-19. In Journal of Medical Systems (Vol. 45, Issue 7). Springer Science and Business Media LLC. https://doi.org/10.1007/s10916-021-01745-4.
Han, Z., Wei, B., Hong, Y., Li, T., Cong, J., Zhu, X., Wei, H., & Zhang, W. (2020). Accurate Screening of COVID-19 Using Attention-Based Deep 3D Multiple Instance Learning. In IEEE Transactions on Medical Imaging (Vol. 39, Issue 8, pp. 2584–2594). Institute of Electrical and Electronics Engineers (IEEE). https://doi.org/10.1109/tmi.2020.2996256.
Hariri, M., & Avşar, E. (2023). COVID-19 and pneumonia diagnosis from chest X-ray images using convolutional neural networks. In Network Modeling Analysis in Health Informatics and Bioinformatics (Vol. 12, Issue 1). Springer Science and Business Media LLC. https://doi.org/10.1007/s13721-023-00413-6.
Hasan, M. D. K., Ahmed, S., Abdullah, Z. M. E., Monirujjaman Khan, M., Anand, D., Singh, A., AlZain, M., & Masud, M. (2021). Deep Learning Approaches for Detecting Pneumonia in COVID-19 Patients by Analyzing Chest X-Ray Images. In K. Sun (Ed.), Mathematical Problems in Engineering (Vol. 2021, pp. 1–8). Hindawi Limited. https://doi.org/10.1155/2021/9929274.
Hasan, N., Bao, Y., Shawon, A., & Huang, Y. (2021). DenseNet Convolutional Neural Networks Application for Predicting COVID-19 Using CT Image. In SN Computer Science (Vol. 2, Issue 5). Springer Science and Business Media LLC. https://doi.org/10.1007/s42979-021-00782-7.
Hashim, A. (2015). Serum VEGF165 and HGF in Egyptian Patients with Lung and Pleural Cancers. ISBN: 978-1-61896-077-1.
Hayat, A., Baglat, P., Mendonça, F., Mostafa, S. S., & Morgado-Dias, F. (2023). Novel Comparative Study for the Detection of COVID-19 Using CT Scan and Chest X-ray Images. In International Journal of Environmental Research and Public Health (Vol. 20, Issue 2, p. 1268). MDPI AG. https://doi.org/10.3390/ijerph20021268.
He, K., Zhang, X., Ren, S., & Sun, J. (2015). Deep Residual Learning for Image Recognition (Version 1). arXiv. https://doi.org/10.48550/ARXIV.1512.03385.
Hemdan, E. E.-D., Shouman, M. A., & Karar, M. E. (2020). CovidX-Net: A Framework of Deep Learning Classifiers to Diagnose COVID-19 in X-Ray Images (Version 1). arXiv. https://doi.org/10.48550/ARXIV.2003.11055.
Hevner, March, Park, & Ram. (2004). Design Science in Information Systems Research. In MIS Quarterly (Vol. 28, Issue 1, p. 75). JSTOR. https://doi.org/10.2307/25148625.
Hevner, A., & Chatterjee, S. (2010). Design Research in Information Systems. In Design Research in Information Systems - Theory and Practice (Vol. 22, pp. 9–23). Springer. https://doi.org/10.1007/978-1-4419-5653-8.
Hu, M., Lin, H., Fan, Z., Gao, W., Yang, L., Liu, C., & Song, Q. (2020). Learning to Recognize Chest-Xray Images Faster and More Efficiently Based on Multi-Kernel Depthwise Convolution. In IEEE Access (Vol. 8, pp. 37265–37274). Institute of Electrical and Electronics Engineers (IEEE). https://doi.org/10.1109/access.2020.2974242.
Ibrahim, A. U., Ozsoz, M., Serte, S., Al-Turjman, F., & Yakoi, P. S. (2021). Pneumonia Classification Using Deep Learning from Chest X-ray Images During COVID-19. In Cognitive Computation. Springer Science and Business Media LLC. https://doi.org/10.1007/s12559-020-09787-5.
Igwebike-Ossi, C. D. (2017). X-Ray Techniques. In Failure Analysis and Prevention. InTech. https://doi.org/10.5772/intechopen.72447.
Islam, N., Mohsin, A. S. M., Choudhury, S. H., Shaer, T. P., Islam, Md. A., Sadat, O., & Taz, N. H. (2024). COVID-19 and Pneumonia detection and web deployment from CT scan and X-ray images using deep learning. In M. Heenaye- Mamode Khan (Ed.), PLOS ONE (Vol. 19, Issue 7, p. e0302413). Public Library of Science (PLoS). https://doi.org/10.1371/journal.pone.0302413.
Ismael, A. M., & Şengür, A. (2021). Deep learning approaches for COVID-19 detection based on chest X-ray images. In Expert Systems with Applications (Vol. 164, p. 114054). Elsevier BV. https://doi.org/10.1016/j.eswa.2020.114054.
Jain, R., Gupta, M., Taneja, S., & Hemanth, D. J. (2020). Deep learning based detection and analysis of COVID-19 on chest X-ray images. In Applied Intelligence (Vol. 51, Issue 3, pp. 1690–1700). Springer Science and Business Media LLC. https://doi.org/10.1007/s10489-020-01902-1.
Jaiswal, A., Gianchandani, N., Singh, D., Kumar, V., & Kaur, M. (2020). Classification of the COVID-19 infected patients using DenseNet201 based deep transfer learning. In Journal of Biomolecular Structure and Dynamics (Vol. 39, Issue 15, pp. 5682–5689). Informa UK Limited. https://doi.org/10.1080/07391102.2020.1788642.
Jamison, D. A., Jr, Anand Narayanan, S., Trovão, N. S., Guarnieri, J. W., Topper, M. J., Moraes- Vieira, P. M., Zaksas, V., Singh, K. K., Wurtele, E. S., & Beheshti, A. (2022). A comprehensive SARS-CoV-2 and COVID-19 review, Part 1: Intracellular overdrive for SARS-CoV-2 infection. European journal of human genetics : EJHG, 1–10. Advance online publication. https://doi.org/10.1038/s41431-022-01108-8.
Jashnani, K., Nargunde, R., Shah, Y., & Raul, N. (2021). COVID-19 Prediction from CT Scans using Deep-Learning. In 2021 International Conference on Communication information and Computing Technology (ICCICT). 2021 International Conference on Communication information and Computing Technology (ICCICT). IEEE. https://doi.org/10.1109/iccict50803.2021.9509936.
Jonibekovich, J. J. (2021). The Role of Computed Tomography in Pneumonia in Patients with Associated Coronavirus Infection. In Middle European Scientific Bulletin (Vol. 13). Academic Journal Development Service. https://doi.org/10.47494/mesb.2021.13.658.
Kamal, M. S., Chowdhury, L., Dey, N., Fong, S. J., & Santosh, K. (2021, October). Explainable AI to analyze outcomes of spike neural network in COVID-19 chest x-rays. In 2021 IEEE International Conference on Systems, Man, and Cybernetics (SMC) (pp. 3408-3415). IEEE.
Karac, A. (2023). Predicting COVID-19 Cases on a Large Chest X-Ray Dataset Using Modified Pre-trained CNN Architectures. Applied Computer Systems,28(1) 44-57. https://doi.org/10.2478/acss-2023-0005.
Kermany, D. (2018). Labeled Optical Coherence Tomography (OCT) and Chest X-Ray Images for Classification [dataset]. Mendeley. https://doi.org/10.17632/RSCBJBR9SJ.2 
Kermany, D. S., Goldbaum, M., Cai, W., Valentim, C. C. S., Liang, H., Baxter, S. L., McKeown, A., Yang, G., Wu, X., Yan, F., Dong, J., Prasadha, M. K., Pei, J., Ting, M. Y. L., Zhu, J., Li, C., Hewett, S., Dong, J., Ziyar, I., Zhang, K. (2018). Identifying Medical Diagnoses and Treatable Diseases by Image-Based Deep Learning. In Cell (Vol. 172, Issue 5, pp. 1122-1131.e9). Elsevier BV. https://doi.org/10.1016/j.cell.2018.02.010.
Khan, A. I., Shah, J. L., & Bhat, M. M. (2020). CoroNet: A deep neural network for detection and diagnosis of COVID-19 from chest x-ray images. In Computer Methods and Programs in Biomedicine (Vol. 196, p. 105581). Elsevier BV. https://doi.org/10.1016/j.cmpb.2020.105581.
Khan, S. H., Sohail, A., Khan, A., & Lee, Y.-S. (2022). COVID-19 Detection in Chest X-ray Images Using a New Channel Boosted CNN. In Diagnostics (Vol. 12, Issue 2, p. 267). MDPI AG. https://doi.org/10.3390/diagnostics12020267.
Khan, S., Islam, S. M. M., Nasib, A. U., Hasnat, F., Hasan, Md. M., Mim, S., Bin Sayed, J., Mehedi, M. H. K., Iqbal, S., & Rasel, A. A. (2022). COVID-19 Classification from X-Ray Images using 2D CNN. In 2022 IEEE 10th Region 10 Humanitarian Technology Conference (R10-HTC). 2022 IEEE 10th Region 10 Humanitarian Technology Conference (R10-HTC). IEEE. https://doi.org/10.1109/r10-htc54060.2022.9929517.
Khvostikov, A., Aderghal, K., Benois-Pineau, J., Krylov, A., & Catheline, G. (2018). 3D CNN-based classification using sMRI and MD-DTI images for Alzheimer disease studies (Version 1). arXiv. https://doi.org/10.48550/ARXIV.1801.05968.
Kitchenham, B. (2004) Procedures for Performing Systematic Reviews. Keele University.
Kordnoori, S., Sabeti, M., Mostafaei, H., & Banihashemi, S. S. A. (2023). An efficient deep multi‐task learning structure for covid‐19 disease. In IET Image Processing (Vol. 17, Issue 13, pp. 3728–3745). Institution of Engineering and Technology (IET). https://doi.org/10.1049/ipr2.12893.
Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2017). ImageNet classification with deep convolutional neural networks. In Communications of the ACM (Vol. 60, Issue 6, pp. 84–90). Association for Computing Machinery (ACM). https://doi.org/10.1145/3065386.
Kumar, N., Hashmi, A., Gupta, M., & Kundu, A. (2022). Automatic Diagnosis of COVID-19 Related Pneumonia from CXR and CT-Scan Images. In Engineering, Technology &amp; Applied Science Research (Vol. 12, Issue 1, pp. 7993–7997). Engineering, Technology & Applied Science Research. https://doi.org/10.48084/etasr.4613.
Kundu, R., Das, R., Geem, Z. W., Han, G.-T., & Sarkar, R. (2021). Pneumonia detection in chest X-ray images using an ensemble of deep learning models. In R. Damaševičius (Ed.), PLOS ONE (Vol. 16, Issue 9, p. e0256630). Public Library of Science (PLoS). https://doi.org/10.1371/journal.pone.0256630.
Kusk, M. W., & Lysdahlgaard, S. (2023). The effect of Gaussian noise on pneumonia detection on chest radiographs, using convolutional neural networks. In Radiography (Vol. 29, Issue 1, pp. 38–43). Elsevier BV. https://doi.org/10.1016/j.radi.2022.09.011.
Lasker, A., Ghosh, M., Obaidullah, S. M., Chakraborty, C., & Roy, K. (2022). LWSNet - a novel deep-learning architecture to segregate COVID-19 and pneumonia from x-ray imagery. In Multimedia Tools and Applications (Vol. 82, Issue 14, pp. 21801–21823). Springer Science and Business Media LLC. https://doi.org/10.1007/s11042-022-14247-3.
Lawton, S., & Viriri, S. (2021). Detection of COVID-19 from CT Lung Scans Using Transfer Learning. In M. Versaci (Ed.), Computational Intelligence and Neuroscience (Vol. 2021, pp. 1–14). Hindawi Limited. https://doi.org/10.1155/2021/5527923.
Lobo, P. (2023) X-ray. Procedure Video | Diagnostic Imaging Procedures Video. https://www.ypo.education/medical-tests/x-ray-t291/video/.
Li, X., Tan, W., Liu, P., Zhou, Q., & Yang, J. (2021). Classification of COVID-19 Chest CT Images Based on Ensemble Deep Learning. In L. Pavone (Ed.), Journal of Healthcare Engineering (Vol. 2021, pp. 1–7). Hindawi Limited. https://doi.org/10.1155/2021/5528441.
Lippi, G., Simundic, A. M., & Plebani, M. (2020). Potential preanalytical and analytical vulnerabilities in the laboratory diagnosis of coronavirus disease 2019 (COVID-19). Clinical Chemistry and Laboratory Medicine (CCLM), 58(7), 1070-1076. https://doi.org/10.1515/cclm-2020-0285"10.1515/cclm-2020-0285.
Loubser, M., & Verryn, S. (2008). Combining XRF and XRD analyses and sample preparation to solve mineralogical problems. In South African Journal of Geology (Vol. 111, Issues 2–3, pp. 229–238). Geological Society of South Africa. https://doi.org/10.2113/gssajg.111.2-3.229.
Mabrouk, A., Díaz Redondo, R. P., Dahou, A., Abd Elaziz, M., & Kayed, M. (2022). Pneumonia Detection on Chest X-ray Images Using Ensemble of Deep Convolutional Neural Networks. In Applied Sciences (Vol. 12, Issue 13, p. 6448). MDPI AG. https://doi.org/10.3390/app12136448.
Mack, N., Woodsong, C., Km, M., Guest, G., & Namey, E. (2005). Qualitative research methods: a data collectors field guide. ISBN: 0939704986.
Mackenzie, G. (2016). The definition and classification of pneumonia. In Pneumonia (Vol. 8, Issue 1). Springer Science and Business Media LLC. https://doi.org/10.1186/s41479-016-0012-z.
Marques, O. (2021). Retrieved from https://github.com/ogemarques/xai-matlab/releases.
Marques, O. (2023). Explainable AI for medical images. File Exchange - MATLAB Central. Retrieved from https://www.mathworks.com/matlabcentral/fileexchange/96647-explainable-ai-for-medical-images.
Masud, M., Dahman Alshehri, M., Alroobaea, R., & Shorfuzzaman, M. (2021). Leveraging Convolutional Neural Network for COVID-19 Disease Detection Using CT Scan Images. In Intelligent Automation &amp; Soft Computing (Vol. 29, Issue 1, pp. 1–13). Computers, Materials and Continua (Tech Science Press). https://doi.org/10.32604/iasc.2021.016800.
Micallef, N., Debono, C. J., Seychell, D., & Attard, C. (2022). Automatic Detection of COVID-19 Pneumonia in Chest Computed Tomography Scans Using Convolutional Neural Networks. In 2022 IEEE 21st Mediterranean Electrotechnical Conference (MELECON). 2022 IEEE 21st Mediterranean Electrotechnical Conference (MELECON). IEEE. https://doi.org/10.1109/melecon53508.2022.9843100.
Mideksa, S., Ababor, S., Gebreyohannes, Y., Bogale, F., Solomon, D., Getachew, T., Ararso, D., Wolde, E., Kebede, Z., & Tollera, G. (2022). PP56 The Use of Computed Tomography for Detecting COVID-19 Pneumonia: Rapid Evidence Review. In International Journal of Technology Assessment in Health Care (Vol. 38, Issue S1, pp. S59–S59). Cambridge University Press (CUP). https://doi.org/10.1017/s0266462322001933.
Militante, S. V., Dionisio, N. V., & Sibbaluca, B. G. (2020). Pneumonia and COVID-19 Detection using Convolutional Neural Networks. In 2020 Third International Conference on Vocational Education and Electrical Engineering (ICVEE). 2020 Third International Conference on Vocational Education and Electrical Engineering (ICVEE). IEEE. https://doi.org/10.1109/icvee50212.2020.9243290.
Minaee, S. (2020). Retrieved from https://github.com/shervinmin/DeepCovid. 
Minaee, S., Kafieh, R., Sonka, M., Yazdani, S., & Jamalipour Soufi, G. (2020). Deep-Covid: Predicting COVID-19 from chest X-ray images using deep transfer learning. In Medical Image Analysis (Vol. 65, p. 101794). Elsevier BV. https://doi.org/10.1016/j.media.2020.101794.
Mohamadou, Y., Halidou, A. & Kapen, P.T. A review of mathematical modeling, artificial intelligence and datasets used in the study, prediction and management of COVID-19. Appl Intell 50, 3913–3925 (2020). https://doi.org/10.1007/s10489-020-01770-9.
Mooney, P. (2018). Retrieved from https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia.
Moreira, C., Nobre, I. B., Sousa, S. C., Pereira, J. M., & Jorge, J. (2022, March). Improving X-ray Diagnostics through Eye-Tracking and XR. In 2022 IEEE Conference on Virtual Reality and 3D User Interfaces Abstracts and Workshops (VRW) (pp. 450-453). IEEE. https://doi.org/10.1109/VRW55335.2022.00099.
Nandagobalan, N. M., & Chaw, J. K. (2023). UTILIZING DEEP LEARNING ON WEB APPLICATION FOR COVID-19 PNEUMONIA DETECTION. In Journal of Information System and Technology Management (Vol. 8, Issue 32, pp. 113–128). Global Academic Excellence (M) Sdn Bhd. https://doi.org/10.35631/jistm.832008.
Narayanan, B. N., Ali, R. A., & Hardie, R. C. (2019). Performance analysis of machine learning and deep learning architectures for malaria detection on cell images. In M. E. Zelinski, T. M. Taha, J. Howe, A. A. Awwal, & K. M. Iftekharuddin (Eds.), Applications of Machine Learning. SPIE. https://doi.org/10.1117/12.2524681.
Narayanan, B., Hardie, R., Krishnaraja, V., Karam, C., & Davuluru, V. (2020). Transfer-to-Transfer Learning Approach for Computer Aided Detection of COVID-19 in Chest Radiographs. In AI (Vol. 1, Issue 4, pp. 539–557). MDPI AG. https://doi.org/10.3390/ai1040032.
Narayan Das, N., Kumar, N., Kaur, M., Kumar, V., & Singh, D. (2022). Automated Deep Transfer Learning-Based Approach for Detection of COVID-19 Infection in Chest X-rays. In IRBM (Vol. 43, Issue 2, pp. 114–119). Elsevier BV. https://doi.org/10.1016/j.irbm.2020.07.001.
Narin, A., Kaya, C., & Pamuk, Z. (2021). Automatic detection of coronavirus disease (COVID-19) using X-ray images and deep convolutional neural networks. In Pattern Analysis and Applications (Vol. 24, Issue 3, pp. 1207–1220). Springer Science and Business Media LLC. https://doi.org/10.1007/s10044-021-00984-y.
Ong, J. H., Goh, K. M., & Lim, L. L. (2021, September). Comparative Analysis of Explainable Artificial Intelligence for COVID-19 Diagnosis on CXR Image. In 2021 IEEE International Conference on Signal and Image Processing Applications (ICSIPA) (pp. 185-190). IEEE.
Ortiz-Toro, C., García-Pedrero, A., Lillo-Saavedra, M., & Gonzalo-Martín, C. (2022). Automatic detection of pneumonia in chest X-ray images using textural features. In Computers in Biology and Medicine (Vol. 145, p. 105466). Elsevier BV. https://doi.org/10.1016/j.compbiomed.2022.105466.
Ouyang, X., Huo, J., Xia, L., Shan, F., Liu, J., Mo, Z., Yan, F., Ding, Z., Yang, Q., Song, B., Shi, F., Yuan, H., Wei, Y., Cao, X., Gao, Y., Wu, D., Wang, Q., & Shen, D. (2020). Dual-Sampling Attention Network for Diagnosis of COVID-19 From Community Acquired Pneumonia. In IEEE Transactions on Medical Imaging (Vol. 39, Issue 8, pp. 2595–2605). Institute of Electrical and Electronics Engineers (IEEE). https://doi.org/10.1109/tmi.2020.2995508.
Ozturk, T., Talo, M., Yildirim, E. A., Baloglu, U. B., Yildirim, O., & Rajendra Acharya, U. (2020). Automated detection of COVID-19 cases using deep neural networks with X-ray images. In Computers in Biology and Medicine (Vol. 121, p. 103792). Elsevier BV. https://doi.org/10.1016/j.compbiomed.2020.103792.
Pandit, M. K., Banday, S. A., Naaz, R., & Chishti, M. A. (2021). Automatic detection of COVID-19 from chest radiographs using deep learning. In Radiography (Vol. 27, Issue 2, pp. 483–489). Elsevier BV. https://doi.org/10.1016/j.radi.2020.10.018.
Panwar, A., Dagar, A., Pal, V., & Kumar, V. (2021). COVID 19, Pneumonia and Other Disease Classification using Chest X-Ray images. In 2021 2nd International Conference for Emerging Technology (INCET). 2021 2nd International Conference for Emerging Technology (INCET). IEEE. https://doi.org/10.1109/incet51464.2021.9456192.
Pathak, Y., Shukla, P. K., Tiwari, A., Stalin, S., Singh, S., & Shukla, P. K. (2022). Deep Transfer Learning Based Classification Model for COVID-19 Disease. In IRBM (Vol. 43, Issue 2, pp. 87–92). Elsevier BV. https://doi.org/10.1016/j.irbm.2020.05.003.
Pedraza, A., Gallego, J., Lopez, S., Gonzalez, L., Laurinavicius, A., & Bueno, G. (2017). Glomerulus Classification with Convolutional Neural Networks. In Communications in Computer and Information Science (pp. 839–849). Springer International Publishing. https://doi.org/10.1007/978-3-319-60964-5_73.
Peffers, K., Tuunanen, T., Gengler, C. E., Rossi, M., Hui, W., Virtanen, V., & Bragge, J. (2020). Design Science Research Process: A Model for Producing and Presenting Information Systems Research. arXiv. https://doi.org/10.48550/ARXIV.2006.02763.
Pitumbur, A. (2023). COVID-19 Detection in Chest X-ray Images Using Explainable Boosting Algorithms  (thesis).
Pham, T. D. (2020). Classification of COVID-19 chest X-rays with deep learning: new models or fine tuning? In Health Information Science and Systems (Vol. 9, Issue 1). Springer Science and Business Media LLC. https://doi.org/10.1007/s13755-020-00135-3.
Polat, H., Özerdem, M. S., Ekici, F., & Akpolat, V. (2021). Automatic detection and localization of COVID‐19 pneumonia using axial computed tomography images and deep convolutional neural networks. In International Journal of Imaging Systems and Technology (Vol. 31, Issue 2, pp. 509–524). Wiley. https://doi.org/10.1002/ima.22558.
Prashant, P. (2020, September 17). Chest X-ray (COVID-19 &amp; pneumonia). Kaggle. Retrieved February 5, 2023, from https://www.kaggle.com/datasets/prashant268/chest-xray-Covid19-pneumonia.
Rahman, T. (2022, March 19). COVID-19 radiography database. Kaggle. Retrieved February 5, 2023, from https://www.kaggle.com/datasets/tawsifurrahman/Covid19-radiography-database.
Rahman, M. M., Nooruddin, S., Hasan, K. M. A., & Dey, N. K. (2021). HOG + CNN Net: Diagnosing COVID-19 and Pneumonia by Deep Neural Network from Chest X-Ray Images. In SN Computer Science (Vol. 2, Issue 5). Springer Science and Business Media LLC. https://doi.org/10.1007/s42979-021-00762-x.
Rakesh, J. (2022). COVID-19 and Other Pneumonia Diagnosis Using CNN. In International Journal for Research in Applied Science and Engineering Technology (Vol. 10, Issue 10, pp. 1519–1525). International Journal for Research in Applied Science and Engineering Technology (IJRASET). https://doi.org/10.22214/ijraset.2022.47.
Ranjan, A., Kumar, C., Gupta, R. K., & Misra, R. (2022). Transfer Learning Based Approach for Pneumonia Detection Using Customized VGG16 Deep Learning Model. In Internet of Things and Connected Technologies (pp. 17–28). Springer International Publishing. https://doi.org/10.1007/978-3-030-94507-7_2.
Reddy, G. B., Greif, D. N., Rodriguez, J., Best, T. M., Greditzer, H. G., 4th, & Jose, J. (2020). Clinical Characteristics and Multisystem Imaging Findings of COVID-19: An Overview for Orthopedic Surgeons. HSS journal: the musculoskeletal journal of Hospital for Special Surgery, 16(Suppl 1), 112–123. https://doi.org/10.1007/s11420-020-09775-3. 
Reshan, M. S. A., Gill, K. S., Anand, V., Gupta, S., Alshahrani, H., Sulaiman, A., & Shaikh, A. (2023). Detection of Pneumonia from Chest X-ray Images Utilizing MobileNet Model. In Healthcare (Vol. 11, Issue 11, p. 1561). MDPI AG. https://doi.org/10.3390/healthcare11111561.
Reshi, A. A., Rustam, F., Mehmood, A., Alhossan, A., Alrabiah, Z., Ahmad, A., Alsuwailem, H., & Choi, G. S. (2021). An Efficient CNN Model for COVID-19 Disease Detection Based on X-Ray Image Classification. In Á. Madureira Bueno (Ed.), Complexity (Vol. 2021, pp. 1–12). Hindawi Limited. https://doi.org/10.1155/2021/6621607.
Ronneberger, O., Fischer, P., & Brox, Thomas. (2015). U-Net: Convolutional Networks for Biomedical Image Segmentation. LNCS. 9351. 234-241. https://doi.org/10.1007/978-3- 319-24574-4_28.
Saeedi, A., Saeedi, M., & Maghsoudi, A. (2020). A novel and reliable deep learning web-based tool to detect COVID-19 infection from chest ct-scan. arXiv preprint arXiv:2006.14419. 
Sait, U. (2021). Curated Dataset for COVID-19 Posterior-Anterior Chest Radiography Images (X-Rays). [dataset]. Mendeley. https://doi.org/10.17632/9XKHGTS2S6.3.
Shailendra. (2020). Retrieved from https://www.kaggle.com/code/shailendra2811/vgg-based-cat-dog-classifier-98-accuracy.
Saboo, Y. S., Kapse, S., & Prasanna, P. (2023). Convolutional Neural Networks (CNNs) for Pneumonia Classification on Pediatric Chest Radiographs. In Cureus. Springer Science and Business Media LLC. https://doi.org/10.7759/cureus.44130.
Sekeroglu, B., & Ozsahin, I. (2020). Detection of COVID-19 from Chest X-Ray Images Using Convolutional Neural Networks. SLAS TECHNOLOGY: Translating Life Sciences Innovation, 25(6), 553–565. https://doi.org/10.1177/2472630320958376.
Selvaraju, R. R., Cogswell, M., Das, A., Vedantam, R., Parikh, D., & Batra, D. (2016). Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization. arXiv. https://doi.org/10.48550/ARXIV.1610.02391.
Shankar, K., Perumal, E., Díaz, V. G., Tiwari, P., Gupta, D., Saudagar, A. K. J., & Muhammad, K. (2021). An optimal cascaded recurrent neural network for intelligent COVID-19 detection using Chest X-ray images. In Applied Soft Computing (Vol. 113, p. 107878). Elsevier BV. https://doi.org/10.1016/j.asoc.2021.107878.
Sharma, S., & Guleria, K. (2023). A Deep Learning based model for the Detection of Pneumonia from Chest X-Ray Images using VGG-16 and Neural Networks. In Procedia Computer Science (Vol. 218, pp. 357–366). Elsevier BV. https://doi.org/10.1016/j.procs.2023.01.018.
Shuja, J., Alanazi, E., Alasmary, W. et al. COVID-19 open source data sets: a comprehensive survey. Appl Intell 51, 1296–1325 (2021). https://doi.org/10.1007/s10489-020-01862-6.
Silva, P., Luz, E., Silva, G., Moreira, G., Silva, R., Lucio, D., & Menotti, D. (2020). COVID-19 detection in CT images with deep learning: A voting-based scheme and cross-datasets analysis. In Informatics in Medicine Unlocked (Vol. 20, p. 100427). Elsevier BV. https://doi.org/10.1016/j.imu.2020.100427.
Simonyan, K., & Zisserman, A. (2014). Very Deep Convolutional Networks for Large-Scale Image Recognition (Version 6). arXiv. https://doi.org/10.48550/ARXIV.1409.1556.
Singh, S., Kumar, M., Kumar, A., Verma, B. K., & Shitharth, S. (2023). Pneumonia detection with QCSA network on chest X-ray. In Scientific Reports (Vol. 13, Issue 1). Springer Science and Business Media LLC. https://doi.org/10.1038/s41598-023-35922-x.
Sitaula, C., & Hossain, M. B. (2020). Attention-based VGG-16 model for COVID-19 chest X-ray image classification. In Applied Intelligence (Vol. 51, Issue 5, pp. 2850–2863). Springer Science and Business Media LLC. https://doi.org/10.1007/s10489-020-02055-x.
Stephen, O., Sain, M., Maduh, U. J., & Jeong, D.-U. (2019). An Efficient Deep Learning Approach to Pneumonia Classification in Healthcare. In Journal of Healthcare Engineering (Vol. 2019, pp. 1–7). Hindawi Limited. https://doi.org/10.1155/2019/4180949.
Sukamolson, S. (2007). Fundamentals of quantitative research. Language Institute Chulalongkorn University, 1(3), 1-20.
Sun, L., Mo, Z., Yan, F., Xia, L., Shan, F., Ding, Z., Song, B., Gao, W., Shao, W., Shi, F., Yuan, H., Jiang, H., Wu, D., Wei, Y., Gao, Y., Sui, H., Zhang, D., & Shen, D. (2020). Adaptive Feature Selection Guided Deep Forest for COVID-19 Classification With Chest CT. In IEEE Journal of Biomedical and Health Informatics (Vol. 24, Issue 10, pp. 2798–2805). Institute of Electrical and Electronics Engineers (IEEE). https://doi.org/10.1109/jbhi.2020.3019505.
Szepesi, P., & Szilágyi, L. (2022). Detection of pneumonia using convolutional neural networks and deep learning. In Biocybernetics and Biomedical Engineering (Vol. 42, Issue 3, pp. 1012–1022). Elsevier BV. https://doi.org/10.1016/j.bbe.2022.08.001.
Taher, F., Haweel, R. T., Al Bastaki, U. M. H., Abdelwahed, E., Rehman, T., & Haweel, T. I. (2022). COVID-19 Detection Based on Chest X-Ray Images Using DCT Compression and NN. In 2022 IEEE International Conference on Imaging Systems and Techniques (IST). 2022 IEEE International Conference on Imaging Systems and Techniques (IST). IEEE. https://doi.org/10.1109/ist55454.2022.9827673.
Tang, Y.-X., Tang, Y.-B., Peng, Y., Yan, K., Bagheri, M., Redd, B. A., Brandon, C. J., Lu, Z., Han, M., Xiao, J., & Summers, R. M. (2020). Automated abnormality classification of chest radiographs using deep convolutional neural networks. In npj Digital Medicine (Vol. 3, Issue 1). Springer Science and Business Media LLC. https://doi.org/10.1038/s41746-020-0273-z.
Topff, L., Sánchez-García, J., López-González, R., Pastor, A. J., Visser, J. J., Huisman, M., Guiot, J., Beets-Tan, R. G. H., Alberich-Bayarri, A., Fuster-Matanzo, A., & Ranschaert, E. R. (2023). A deep learning-based application for COVID-19 diagnosis on CT: The Imaging COVID-19 AI initiative. In C. Casà (Ed.), PLOS ONE (Vol. 18, Issue 5, p. e0285121). Public Library of Science (PLoS). https://doi.org/10.1371/journal.pone.0285121.
Toraman, S., Alakus, T. B., & Turkoglu, I. (2020). Convolutional capsnet: A novel artificial neural network approach to detect COVID-19 disease from X-ray images using capsule networks. In Chaos, Solitons &amp; Fractals (Vol. 140, p. 110122). Elsevier BV. https://doi.org/10.1016/j.chaos.2020.110122.
Turkoglu, M. (2020). CovidetectioNet: COVID-19 diagnosis system based on X-ray images using features selected from pre-learned deep features ensemble. In Applied Intelligence (Vol. 51, Issue 3, pp. 1213–1226). Springer Science and Business Media LLC. https://doi.org/10.1007/s10489-020-01888-w.
Ucar, F., & Korkmaz, D. (2020). Covidiagnosis-Net: Deep Bayes-SqueezeNet based diagnosis of the coronavirus disease 2019 (COVID-19) from X-ray images. In Medical Hypotheses (Vol. 140, p. 109761). Elsevier BV. https://doi.org/10.1016/j.mehy.2020.109761.
Ulutas, H., Sahin, M. E., & Karakus, M. O. (2023). Application of a novel deep learning technique using CT images for COVID-19 diagnosis on embedded systems. In Alexandria Engineering Journal (Vol. 74, pp. 345–358). Elsevier BV. https://doi.org/10.1016/j.aej.2023.05.036.
Varshni, D., Thakral, K., Agarwal, L., Nijhawan, R., & Mittal, A. (2019). Pneumonia Detection Using CNN based Feature Extraction. In 2019 IEEE International Conference on Electrical, Computer and Communication Technologies (ICECCT). 2019 IEEE International Conference on Electrical, Computer and Communication Technologies (ICECCT). IEEE. https://doi.org/10.1109/icecct.2019.8869364.
Waheed, A., Goyal, M., Gupta, D., Khanna, A., Al-Turjman, F., & Pinheiro, P. R. (2020). Covidgan: data augmentation using auxiliary classifier gan for improved COVID-19 detection. IEEE Access, 8, 91916-91923. https://doi.org/10.1109/ACCESS.2020.2994762.
Wang, T., Nie, Z., Wang, R., Xu, Q., Huang, H., Xu, H., Xie, F., & Liu, X.-J. (2023). PneuNet: deep learning for COVID-19 pneumonia diagnosis on chest X-ray image analysis using Vision Transformer. In Medical &amp; Biological Engineering &amp; Computing (Vol. 61, Issue 6, pp. 1395–1408). Springer Science and Business Media LLC. https://doi.org/10.1007/s11517-022-02746-2.
Wang, J., Bao, Y., Wen, Y., Lu, H., Luo, H., Xiang, Y., Li, X., Liu, C., & Qian, D. (2020). Prior-Attention Residual Learning for More Discriminative COVID-19 Screening in CT Images. In IEEE Transactions on Medical Imaging (Vol. 39, Issue 8, pp. 2572–2583). Institute of Electrical and Electronics Engineers (IEEE). https://doi.org/10.1109/tmi.2020.2994908.
Wang, L., Lin, Z. Q., & Wong, A. (2020). Covid-Net: a tailored deep convolutional neural network design for detection of COVID-19 cases from chest X-ray images. In Scientific Reports (Vol. 10, Issue 1). Springer Science and Business Media LLC. https://doi.org/10.1038/s41598-020-76550-z. 
Waterer, G. (2021). What is pneumonia? In Breathe (Vol. 17, Issue 3, p. 210087). European Respiratory Society (ERS). https://doi.org/10.1183/20734735.0087-2021.
Watkinson, N., Givargis, T., Joe, V., Nicolau, A., & Veidenbaum, A. (2021). Detecting COVID-19 Related Pneumonia On CT Scans Using Hyperdimensional Computing. In 2021 43rd Annual International Conference of the IEEE Engineering in Medicine &amp; Biology Society (EMBC). 2021 43rd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC). IEEE. https://doi.org/10.1109/embc46164.2021.9630898.
Widodo, S., Sulistiyanti, A., & Yudistira, I. A. (2022). Detection of COVID-19 on Localized Ct-scan Images Using Deep Learning Convolution Neural Network. In International Journal of Advanced Engineering and Management Research (Vol. 07, Issue 02, pp. 116–129). International Journal of Medical Science and Health Research. https://doi.org/10.51505/ijaemr.2022.7209.
Willer, K., Fingerle, A. A., Noichl, W., De Marco, F., Frank, M., Urban, T., Schick, R., Gustschin, A., Gleich, B., Herzen, J., Koehler, T., Yaroshenko, A., Pralow, T., Zimmermann, G. S., Renger, B., Sauter, A. P., Pfeiffer, D., Makowski, M. R., Rummeny, E. J., Pfeiffer, F. (2021). X-ray dark-field chest imaging for detection and quantification of emphysema in patients with chronic obstructive pulmonary disease: a diagnostic accuracy study. In The Lancet Digital Health (Vol. 3, Issue 11, pp. e733–e744). Elsevier BV. https://doi.org/10.1016/s2589-7500(21)00146-1.
Yamac, M., Ahishali, M., Degerli, A., Kiranyaz, S., Chowdhury, M. E. H., & Gabbouj, M. (2021). Convolutional Sparse Support Estimator-Based COVID-19 Recognition From X-Ray Images. In IEEE Transactions on Neural Networks and Learning Systems (Vol. 32, Issue 5, pp. 1810–1820). Institute of Electrical and Electronics Engineers (IEEE). https://doi.org/10.1109/tnnls.2021.3070467.
Yasar, H., & Ceylan, M. (2020). A novel comparative study for detection of COVID-19 on CT lung images using texture analysis, machine learning, and deep learning methods. In Multimedia Tools and Applications (Vol. 80, Issue 4, pp. 5423–5447). Springer Science and Business Media LLC. https://doi.org/10.1007/s11042-020-09894-3.
Ye, Q., Xia, J., & Yang, G. (2021, June). Explainable AI for COVID-19 CT classifiers: An initial comparison study. In 2021 IEEE 34th International Symposium on Computer-Based Medical Systems (CBMS) (pp. 521-526). IEEE.
Zeiser, F. A., Costa, C. A. da, Ramos, G. de O., Bohn, H., Santos, I., & Righi, R. da R. (2021). Evaluation of Convolutional Neural Networks for COVID-19 Classification on Chest X-Rays. In Intelligent Systems (pp. 121–132). Springer International Publishing. https://doi.org/10.1007/978-3-030-91699-2_9.
Zukauskas, P.,   Vveinhardt, J.   &   Andriukaitienė, R.   (2018).   Exploratory   Research. https://doi.org/10.5772/intechope.
Zhang, A. (2020). COVID-19 Chest X-ray Images: Lung Segmentation and Diagnosis using Neural Networks. International Journal on Computational Science & Applications. http://dx.doi.org/10.5121/ijcsa.2020.10501.
Zhang, J., & Zong, C. (2015). Deep Neural Networks in Machine Translation: An Overview. IEEE Intelligent Systems, 30, 16-25. https://doi.org/10.1109/MIS.2015.69.




























