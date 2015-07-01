MAIN = main
TITLE = title
TEX = pdflatex -interaction=nonstopmode
ERROR_PARSING = grep -v "Fancyhdr\|minitoc\|hyperref" | grep -v "Font Warning\|contains only float\|float specifier changed\|fig:'" | grep "Warning\|Error\|^l." | grep -A1 "Warning\|Error" 1>&2

pdf : $(MAIN).pdf

$(MAIN).pdf : $(MAIN).tex ../thesis.tex 
#	$(TEX) $(MAIN).tex
	$(TEX) $(MAIN).tex | $(ERROR_PARSING); mv $(MAIN).pdf ../thesis.pdf
#	$(TEX) $(MAIN).tex | $(ERROR_PARSING); dvipdf $(MAIN).dvi $(MAIN).pdf; pdfunite $(TITLE).pdf $(MAIN).pdf ../thesis.pdf

clean :
	rm -f *.aux *.log *.out *.dvi *.pdf
