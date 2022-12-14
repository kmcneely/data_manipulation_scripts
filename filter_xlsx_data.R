#Filter xlsx by column
#Select the excel sheet and column to filter by by editing "sheet" on line 7 and
#column name (currently "MRN") on line 10
library(tidyverse)
library(readxl)

all_data <- read_xlsx("/path_to_data.xlsx", col_names=TRUE, sheet="Master", col_types = "text")
filter_list <-c(readLines("/path_to_filter_list.csv"))

filtered_data <- subset(all_data, MRN %in% filter_list)
write.csv(filtered_data, file="/path_to_output_file/output_filename.csv", row.names = FALSE)







