NAME := microapptest
PY := python3

pacedb: e3smlab
	@echo "Testing pacedb"
	pytest test_pacedb.py -v

e3smlab: microapp
	@echo "Testing e3smlab"

microapp:
	@echo "Testing microapp"
