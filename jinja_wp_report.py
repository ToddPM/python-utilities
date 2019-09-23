from jinja2 import Template
from weasyprint import HTML


def write_html(html_path, html_line):
  #==========================================================
  #***  Add one line of HTML to the ongoing HTML string.  ***
  #==========================================================
    global html_report

    # Uncomment these to also create an HTML file identical to the PDF being generated.
    #html_file = open(html_path, 'at+')
    #html_file.write(html_line + '\n')
    #html_file.close()

    html_report += html_line

    return  #write_html


program_directory = '\\\\path\\to\\directory'
output_directory = program_directory + '\\output'

my_logo = '<img src="logo.png" alt="logo" height="123" width="185">'

program_html = output_directory + '\\sample_report.html'
program_pdf = output_directory + '\\sample_report.pdf'

head_open = '<!DOCTYPE html><html lang = "en"><head><title>Sample Report</title><style>'
head_close = '</style></head>'
body_open = '<body>'
body_close = '</body></html>'
css = """@page
    {
    size: Letter;
    margin: 0.5cm;
    }

body
	{
	color-adjust:exact;
	font-family: Arial, Helvetica, sans-serif;
	}

p.footer
	{
	font-weight: bold;
	text-align: center;
	}

table.header
	{
	border: 0px;
	width: 100%;
	}

table.data
	{
	border: 1px solid black;
	border-collapse: collapse;
	width: 100%;
	}

td.data
	{
	border: 1px solid black;
	padding-bottom:10px;
	padding-left:10px;
	padding-right:10px;
	padding-top:10px;
	text-align: right;
	}

td.data_header
	{
	background: #94E1BA;
	border: 1px solid black;
	font-weight: bold;
	padding-bottom:10px;
	padding-left:0px;
	padding-right:0px;
	padding-top:10px;
	text-align: center;
	}

td.data_row_header
	{
	background: #94E1BA;
	border: 1px solid black;
	font-weight: bold;
	padding-bottom:10px;
	padding-left:10px;
	padding-right:10px;
	padding-top:10px;
	text-align: left;
	}

td.header
	{
	text-align: left;
	vertical-align: top;
	}"""

#========================================================================
#***  For HTML generation, .PNG location is relative to output file.  ***
#***  For PDF generation, .PNG location is relative to this program.  ***
#========================================================================
template_report_header = Template("""<table CLASS = "header">
		<tr>
			<td CLASS = "header" WIDTH = "10%">&nbsp;</td>
			<td CLASS = "header" WIDTH = "23%">{{ logo }}</td>
			<td CLASS = "header" WIDTH = "10%">&nbsp;</td>
			<td CLASS = "header" WIDTH = "57%">
				<p>{{ title_text }}</p>
			</td>
		</tr>
	</table>""")

template_table_header = Template("""<table CLASS = "data">
		<tr>
			<td CLASS = "data_row_header">Sales Rep</td>
			<td CLASS = "data_header">Q1</td>
			<td CLASS = "data_header">Q2</td>
			<td CLASS = "data_header">Q3</td>
			<td CLASS = "data_header">Q4</td>
		</tr>""")

template_table_row = Template("""<tr>
			<td CLASS = "data_row_header">{{ rep_name }}</td>
			<td CLASS = "data">{{ data_q1 }}</td>
			<td CLASS = "data">{{ data_q2 }}</td>
			<td CLASS = "data">{{ data_q3 }}</td>
			<td CLASS = "data">{{ data_q4 }}</td>
		</tr>""")

template_report_footer = Template("""</table>

	<p CLASS = "footer">This data is complete as of {{ report_date }}.</p>""")

# Print one report.
html_report = ''

write_html(program_html, head_open)
write_html(program_html, css)
write_html(program_html, head_close)
write_html(program_html, body_open)

body = template_report_header.render(title_text = "This sample report was constructed using Jinja2 and WeasyPrint", logo = my_logo)
write_html(program_html, body)

body = template_table_header.render()
write_html(program_html, body)

body = template_table_row.render(rep_name = 'Alice Anderson',
                                data_q1 = 1303,
                                data_q2 = 567,
                                data_q3 = 2501,
                                data_q4 = 1200)
write_html(program_html, body)

body = template_table_row.render(rep_name = 'Bert Brentworth',
                                data_q1 = 455,
                                data_q2 = 1320,
                                data_q3 = 0,
                                data_q4 = 1473)
write_html(program_html, body)

body = template_table_row.render(rep_name = 'Carol Calico',
                                data_q1 = 890,
                                data_q2 = 962,
                                data_q3 = 833,
                                data_q4 = 1078)
write_html(program_html, body)

body = template_table_row.render(rep_name = 'Daniel Dyers',
                                data_q1 = 1004,
                                data_q2 = 2154,
                                data_q3 = 1687,
                                data_q4 = 934)
write_html(program_html, body)

body = template_report_footer.render(report_date = "01/01/2019")
write_html(program_html, body)

write_html(program_html, body_close)

HTML(string = html_report, base_url = '.').write_pdf(program_pdf)
