#How to

Install Python dan Pip

lalu ketik di terminal pada folder tersebut

>pip install -r requirements.txt

#RUN 

Run biasa

>behave features/tests/appcenter.feature

Run dengan report allure framework

>behave -f allure_behave.formatter:AllureFormatter -o reports/ features/tests/appcenter.feature

untuk membuka report dengan cara

>allure serve reports/