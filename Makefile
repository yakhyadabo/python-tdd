default: test

test: 
	@python -m test.test_calculator

run:
	@python -m src.calculator
