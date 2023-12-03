class GetHealthStatusUseCase:
    def __init__(self, health_service):
        self.health_service = health_service

    def execute(self):
        return self.health_service.get_health_status()
