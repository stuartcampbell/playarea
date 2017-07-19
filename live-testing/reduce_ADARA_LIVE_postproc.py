from datetime import datetime

#Now get the counts of the first spectra
count=input.readY(0).sum()
#output it as a log message
logger.notice("Total counts so far " + str(count))

#if my ouput workspace has not been created yet, create it.
if not mtd.doesExist(output):
        table=CreateEmptyTableWorkspace(OutputWorkspace=output)
        table.setTitle("Event Rate History")
        table.addColumn("str", "Time")
        table.addColumn("int", "Events")

table = mtd[output]

table.addRow([datetime.now().isoformat(), int(count)])

