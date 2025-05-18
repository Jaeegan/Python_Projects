# By default the program breaks when an unexpected error occurs
is_even <- function(n) {
  n %% 3 == 0
  print("program contiues without breaking")
}

is_even("Hello")

# try() returns error, and continues the next line without breaking the program
is_even <- function(n) {
  try(n %% 3 == 0)
  print("program contiues without breaking")
}

is_even("Hello")

# tryCatch() returns user specified handler when conditions (error) are met
# flow of execution is interrupted once a handler is called
is_even_error <- function(n) {
  tryCatch(n %% 3 == 0,
    error = function(e) {
      "Invalid input"
    },
    error = function(e) {
      "This will not be printed when a handler is called"
    }
  )
}

is_even_error("Hello")


# A function that returns a message
is_message <- function(m) {
  message(m)
}

is_message("This is my message")

# tryCatch() returns specified handler while,
# withCallingHandlers() ignores the specified handler
tryCatch(is_message("This is my message"),
  message = function(c) {
    "Caught a message!"
  }
)

withCallingHandlers(is_message("This is my message"),
  message = function(c) {
    "Caught a message!"
  }
)
