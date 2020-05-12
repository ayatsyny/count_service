# count_service

This service show count autorization users in your site. This project include demo for count_service application.
If you want to use this service, you need doing the following steps:

- add application **count_service** in you Django project
- add middleware in you Django project, after middleware 'django.middleware.clickjacking.XFrameOptionsMiddleware'
```python
django.middleware.clickjacking.XFrameOptionsMiddleware,
apps.count_service.middelware.IPAccessMiddleware
```
- add variables in you Django settings.py
```python

LOG_PATH
LOG_FILE_NAME
```
- load visit_count in your template 
```html
{% load visit_count %}
```
- add this tag to your html template
```html
{{ request.path|page_count }}
```
