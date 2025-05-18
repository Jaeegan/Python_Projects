
# Load packages
library("fs")
library("usethis")
library("devtools")

setwd("~/R/Repositories/areacalc")

# View the directory structure of the package
dir_tree()

# Create new script `filename`
# use_r("filename")

# Load package to environment
load_all()

# Update documentations and write namespace where `@export` tag is specified
document()

# Submit package to repository
build()

install("~/Documents/R/Repositories/areacalc")

install.packages("~/Documents/R/Repositories/areacalc_0.0.1.tar.gz", type = "source")

library("areacalc")

sq <- square(3)

area(sq)
