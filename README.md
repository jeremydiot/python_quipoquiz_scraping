# python_quipoquiz_scraping

Scraping [QuipoQuiz](https://quipoquiz.com/) site.

## Requirements
- Python3

## Use
```bash
# from projet main folder execute command below

$ ./init.sh
$ cat out/extract.json
```

## API
- Base URL : https://quipoquiz.com/module/sed/quiz/fr
- Select and Get quiz question : /start_quiz.snc?quiz=**{quiz_id}**
- Answer question : /answer_question.snc?quiz=**{quiz_id}**&answer=**{true || false}**&question=**{question_id}**
- Finish quiz and get result : /end_quiz.snc?quiz=**{quiz_id}**