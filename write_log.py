import time

def report_time(seconds):
  #========================================================
  #***  Return a tuple describing the supplied seconds  ***
  #***  value in the most appropriate format.           ***
  #========================================================
    if seconds < 60:
        return_time = seconds
        return_unit = 'seconds'
    elif seconds < (60 * 60):
        return_time = seconds / 60
        return_unit = 'minutes'
    else:
        return_time = seconds / (60 * 60)
        return_unit = 'hours'

    return (return_time, return_unit)  #report_time


def write_log(log_path, log_time, log_line):
  #========================================================
  #***  Write one line to the log. If log_time = True,  ***
  #***  prepend the line with the current time.         ***
  #========================================================
    log_file = open(log_path, 'at+')

    if log_time:
        log_line = '[ ' + time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()) + ' ] ' + log_line

    log_file.write(log_line + '\n')
    log_file.close()

    return  #write_log


program_name = 'sample_program'

program_directory = '\\\\path\\to\\directory'
log_directory = program_directory + '\\logs'

program_start = time.localtime()
log_start = time.time()
stamp = '%Y%m%d_%H%M%S'

program_log = log_directory + '\\' + program_name + '_' + time.strftime(stamp, program_start) + '.log'

write_log(program_log, True, '----- PROGRAM START --- [ ' + program_name + ' ] -----')

#=======================
#***  Program here.  ***
#=======================

log_end = time.time()
read_time, read_unit = report_time(log_end - log_start)
write_log(program_log, True, 'program time: %5.3f %s' % (read_time, read_unit))
write_log(program_log, True, '----- PROGRAM END ----- [ ' + program_name + ' ] -----')
