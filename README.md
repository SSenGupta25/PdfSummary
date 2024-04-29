# PdfSummary

Have a Conversation with Your PDFs! Unveiling the Tech Behind the Magic

This project cuts through the clutter, letting you chat with your PDFs and get answers in plain English! Here's a peek behind the curtain to see how it all works:

* Think of Streamlit as the friendly face.** This tech helps build the user interface, the part you see on your screen where you upload PDFs and ask questions. It's like your personal assistant for navigating the project.
* Extracting the knowledge from PDFs. Libraries like PyPDF2 act like super-powered text scanners, pulling out all the information from those PDFs. Now we have a giant block of text, ready for further exploration.
* Chunking it down – making big data manageable. Imagine trying to read a giant encyclopedia all at once! Libraries like langchain.text_splitter come in to break the text down into smaller, bite-sized chunks. This makes it easier for the next step – the amazing AI part!
* Understanding the meaning – the power of AI. This is where things get exciting! Technologies like GoogleGenerativeAIEmbeddings turn those text chunks into a special code, like a secret language, that captures the ideas within. Then, FAISS, a super-fast search engine, helps find similar pieces of "code" based on your questions.
* Chatting with a super-powered brain – the magic of generative AI models. Imagine a super-smart friend who's read all those PDFs. ChatGoogleGenerativeAI, powered by Google's AI models (like "Gemini-pro" in this case), acts like that friend. It takes the relevant text chunks (found by FAISS) and your question and uses its incredible knowledge to craft clear and concise answers in a conversational style.

This project is all about harnessing the power of technology to make information in PDFs more accessible. It's like having a personal research assistant at your fingertips, helping you find the information you need quickly and easily!

Two files have been uploaded with one having the code and the other is the requirements.txt file> To run the code better to create your own environment of condas and install the requirements then only you can run the code efficiently. 
