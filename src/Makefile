#######################################################
 # Název projektu: Kalkulačka
 # Soubor: Makefile
 # Datum: 2.4.2023
 # Poslední změna: 22.4.2023
 # Autor: Monika Zahradnikova
 # Tým: Tomojavo
#######################################################

MAIN=main.py
PROFILE=profiling.py
TESTS=IMath_tests.py
ZIP=xdolak09_xjerab28_xteich02_xzahra33
DIR_DOC=../../doc
PYTHON=python3
PACKAGES=$(PYTHON) $(PYTHON)-pip $(PYTHON)-tk doxygen graphviz
PROF_INPUT10=../profiling/10in
PROF_INPUT1000=../profiling/1000in
PROF_INPUT1000000=../profiling/1000000in
PATH_FROM_SRC=../../../
INSTALLATOR=TOMOJAVO_CALC-1.0-Linux.deb
INSTALLATOR_PROF=tomojavoprof-1-0-0.deb
BUILD_DIR=build/
ICON_INSTALL=TomojavoCalc.desktop.in
ICON=icon.ico
EXCLUDE_DIR_PROF=tomojavoprof-1-0-0/
EXCLUDE_CMAKE=CMakeLists.txt
EXCLUDE_DOC=doc/html

FROM_SRC=../


.PHONY: all build pack clean test doc run profile

#přeloží projekt – včetně programu pro profiling
all: build doc

#nainstaluje python3, pip a potřebné balíčky
build:
	sudo apt-get update
	sudo apt-get install $(PACKAGES)

#zabalí projekt tak, aby mohl být odevzdán
pack: doc clean
	sudo apt-get install zip
	rm -rf $(PATH_FROM_SRC)$(ZIP) $(PATH_FROM_SRC)$(ZIP).zip
	mkdir $(PATH_FROM_SRC)$(ZIP)
	mkdir $(PATH_FROM_SRC)$(ZIP)/install
	mkdir $(PATH_FROM_SRC)$(ZIP)/doc
	mkdir $(PATH_FROM_SRC)$(ZIP)/repo
	rsync -a ../../.git $(PATH_FROM_SRC)$(ZIP)/repo
	cp $(FROM_SRC)$(ICON_INSTALL) $(PATH_FROM_SRC)$(ZIP)/install
	cp $(FROM_SRC)$(ICON) $(PATH_FROM_SRC)$(ZIP)/install
	cp $(FROM_SRC)$(BUILD_DIR)$(INSTALLATOR) $(PATH_FROM_SRC)$(ZIP)/install
	cp $(FROM_SRC)$(INSTALLATOR_PROF) $(PATH_FROM_SRC)$(ZIP)/install
	cp -r $(DIR_DOC)/html $(PATH_FROM_SRC)$(ZIP)/doc
	rsync -avz --exclude="$(ICON_INSTALL)" --exclude="$(ICON)" --exclude="$(BUILD_DIR)" --exclude="$(EXCLUDE_DIR_PROF)" --exclude="$(EXCLUDE_CMAKE)" --exclude="$(INSTALLATOR_PROF)" --exclude="doc/html" ../ $(PATH_FROM_SRC)$(ZIP)/repo/
	cd $(PATH_FROM_SRC) && zip -r $(ZIP).zip ./$(ZIP)
	rm -rf $(PATH_FROM_SRC)$(ZIP)

#smaže všechny soubory, co nemají být odevzdány
clean:
	rm -rf ../.vscode ../__pycache__ __pycache__ ../profiling/*.prof

#spustí testy matematické knihovny
test:$(TESTS)
	$(PYTHON) $(TESTS)

#spustí generování dokumentace
doc:Doxyfile
	rm -rf $(DIR_DOC)
	mkdir $(DIR_DOC)
	doxygen Doxyfile

#spustí program
run:$(MAIN)
	$(PYTHON) $(MAIN)

#spustí překlad programu a pak samotný program pro výpočet směrodatné odchylky
profile: build $(PROFILE)
	$(PYTHON) $(PROFILE)<$(PROF_INPUT10)
	$(PYTHON) $(PROFILE)<$(PROF_INPUT1000)
	$(PYTHON) $(PROFILE)<$(PROF_INPUT1000000)