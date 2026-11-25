# latexmk configuration. Usage: latexmk           (draft -> build/main.pdf)
#                          THESIS_MODE=final latexmk  (final look, fails on open TODO/TBC)
# Prefer tools/thesis.py for named, versioned PDFs.
use Cwd;
$pdf_mode = 5;                      # xelatex
$xelatex = 'xelatex -interaction=nonstopmode -file-line-error -halt-on-error -synctex=1 %O %S';
$biber = 'biber --validate-datamodel %O %S';
$out_dir = 'build';
$max_repeat = 8;
@default_files = ('main.tex');
$clean_ext = 'bbl run.xml synctex.gz xdv lol loa';
ensure_path('TEXINPUTS', './tex//', './build//');

# version.tex: never edited by hand
my $ver = `git describe --tags --always --dirty --match "v*" 2>${\ ($^O eq 'MSWin32' ? 'NUL' : '/dev/null')}`;
chomp $ver; $ver = 'unversioned' if $ver eq '';
my $sha = `git rev-parse --short=10 HEAD 2>${\ ($^O eq 'MSWin32' ? 'NUL' : '/dev/null')}`;
chomp $sha; $sha = 'none' if $sha eq '';
my $mode = $ENV{'THESIS_MODE'} || 'draft';
mkdir 'build' unless -d 'build';
my $text = "\\gdef\\ThesisVersion{$ver}\n\\gdef\\ThesisCommit{$sha}\n\\gdef\\ThesisMode{$mode}\n";
my $old = '';
if (open(my $in, '<', 'build/version.tex')) { local $/; $old = <$in>; close $in; }
if ($old ne $text) { open(my $fh, '>', 'build/version.tex') or die $!; print $fh $text; close $fh; }
1;
