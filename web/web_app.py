from flask import Flask, request, render_template, make_response

from calculator import CalculatorService
from calculator.exceptions import CalculatorZeroDevisionError
from .forms import CalculatorForm


class WebApp():

    def __init__(
        self,
        calculator_service: CalculatorService,
    ) -> None:
        self.calculator_service = calculator_service
        template_dir = "web/templates"
        static_folder = "web/static"
        self.app = Flask('calc', template_folder=template_dir, static_folder=static_folder)
        self.configure_router()
        self.register_error_handlers()

    def run(self):
        self.app.run(debug=True, host="0.0.0.0")

    def configure_router(self):
        @self.app.get("/")
        def index():
            return render_template("index.html")

        @self.app.post("/calc/")
        def calc():
            form = CalculatorForm(request.form)
            if not form.validate():
                response = make_response(form.errors)
                response.status_code = 400
                return response
            
            answer = self.calculator_service.calculate(
                form.operand_a.data,
                form.operand_b.data,
                form.operator.data,
            )
            return render_template("answer.html", answer=answer)

    def register_error_handlers(self):
        @self.app.errorhandler(CalculatorZeroDevisionError)
        def calculator_zero_devision_error_handler(e: CalculatorZeroDevisionError):
            return str(e), 400
