from notification_service.celery import app


@app.task(bind=True, retry_backoff=True)
def send_message(self):
    print(self)
    print("Запуск задачи на отправку сообщений")