MAIN = main
TITLE = title
TEX = pdflatex -interaction=nonstopmode
ERROR_PARSING = grep -v "Non-PDF special ignored\|Overfull\|Underfull\|float specifier changed" | grep "\\\.box\|\!\|^l\.\|^  \|Reference" 1>&2

pdf : $(MAIN).pdf

$(MAIN).pdf : $(MAIN).tex ../thesis.tex 
#	$(TEX) $(MAIN).tex
	$(TEX) $(MAIN).tex | $(ERROR_PARSING); mv $(MAIN).pdf ../thesis.pdf
#	$(TEX) $(MAIN).tex | $(ERROR_PARSING); dvipdf $(MAIN).dvi $(MAIN).pdf; pdfunite $(TITLE).pdf $(MAIN).pdf ../thesis.pdf

clean :
	rm -f *.aux *.log *.out *.dvi *.pdf
