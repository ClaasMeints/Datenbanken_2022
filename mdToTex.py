with open('./Gliederung.md', 'r') as f:
    lines = f.readlines()
    sections = filter(lambda x: x.startswith('# '), lines)
    
    for i, section in enumerate(sections):
        with open('chapters/' + str(i + 1) + ' ' + section.strip('# ').strip() + '.tex', 'w') as tex:
            tex.write('\chapter{' + section.strip('# ').strip() + '}\label{ch:' + section.strip('# ').strip() + '}\n')
            if i + 1 == 1:
                tex.write('\pagenumbering{arabic}\n')
            for line in lines[lines.index(section) + 1:]:
                if line.startswith('# '):
                    break
                elif line.startswith('## '):
                    tex.write('\section{' + line.strip('# ').strip() + '}\label{sec:' + line.strip('# ').strip() + '}\n')
                elif line.startswith('### '):
                    tex.write('\subsection{' + line.strip('# ').strip() + '}\label{subsec:' + line.strip('# ').strip() + '}\n')
                elif line.startswith('%') or line.startswith('-'):
                    tex.write(line.strip('\n').strip() + '\\\\\n')