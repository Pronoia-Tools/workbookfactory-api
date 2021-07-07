The Django app is called "Workbooks". You can see it here: https://workbookfactory-api.herokuapp.com/workbook-factory/admin/workbooks/ - Each model is represented in that admin panel.

Models
Workbooks
Django Admin Link: https://workbookfactory-api.herokuapp.com/workbook-factory/admin/workbooks/workbook/
API Link: https://workbookfactory-api.herokuapp.com/api/v1/workbooks
Can have content
Can be archived
Must have an owner

Chapters
Django Admin Link: https://workbookfactory-api.herokuapp.com/workbook-factory/admin/workbooks/chapter/
API Link: https://workbookfactory-api.herokuapp.com/api/v1/chapters
Can have content
Can be archived
Can belong to multiple Workbooks
Must have an owner

Pages
Django Admin Link: https://workbookfactory-api.herokuapp.com/workbook-factory/admin/workbooks/page/
API Link: https://workbookfactory-api.herokuapp.com/api/v1/pages
Can have content
Can be archived
Can belong to multiple Chapters
Must have an owner

Questions
Django Admin Link: https://workbookfactory-api.herokuapp.com/workbook-factory/admin/workbooks/question/
API Link: https://workbookfactory-api.herokuapp.com/api/v1/questions
Can have a question
Can be archived
Can belong to multiple Pages
Must have an owner

Answers
Django Admin Link: https://workbookfactory-api.herokuapp.com/workbook-factory/admin/workbooks/answer/
API Link: https://workbookfactory-api.herokuapp.com/api/v1/answers
Has a single answer
Can be archived
Can belong to one question
Must have an owner

API Calls
When calling an endpoint you will get all its children. So, if you call a workbook, you will get all the chapters, pages, questions, and answers as well. If you call a chapter, you will get all the pages, questions, and answers. The further down the tree you go, the smaller the call will be. I did this as a convenience method and NOT as a way that the API "should work". If you want me to flatten things, or return less, or only return the call in question, let me know. One note, the reason that I did it this way is so that, when you call a workbook, you can load everything with one HTTP call instead of a call for each object. Then you can manage what loads when in the frontend and have much tighter control over what appears and how fast.
