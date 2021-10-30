.SILENT:

reload:
	uvicorn main:app --reload

test:
	pytest -s -v