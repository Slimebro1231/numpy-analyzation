# Convert the 'theta' column from degrees to radians
data <- data1
data$θ <- as.numeric(data$θ) * pi / 180

# Splitting the data
data_1 <- data[data$t <= 2.49, ]
data_2 <- data[data$t > 2.5 & data$t <= 4.0, ]

# Define functions for curve fitting
func_1 <- function(t, angular_accel, initial_angle) {
  return(0.5 * angular_accel * t^2 + initial_angle)
}

func_2 <- function(t, angular_accel, initial_velocity, initial_angle) {
  return(0.5 * angular_accel * t^2 + initial_velocity * t + initial_angle)
}

# Curve fitting using nls
fit_1 <- nls(θ ~ func_1(t, angular_accel, initial_angle), 
             data = data_1, 
             start = list(angular_accel = -16.7813, initial_angle = -48.723))

fit_2 <- nls(θ ~ func_2(t, angular_accel, initial_velocity, initial_angle), 
             data = data_2, 
             start = list(angular_accel = -3.5743, initial_velocity = 0, initial_angle = -48.723))

# Predicted values
data_1$fit <- predict(fit_1)
data_2$fit <- predict(fit_2)

# Plotting with enhanced formatting
plot(data$t, data$θ, col = "#e0147c", xlab = "Time (seconds)", ylab = expression(theta), 
     main = "Angular Displacement Over Time", ylim = range(data$θ, data_1$fit, data_2$fit))
lines(data_1$t, data_1$fit, col = "blue", lty = 2)
lines(data_2$t, data_2$fit, col = "black")
abline(v = c(0, 2.5, 4), lty = 2, col = "grey")
# text(4.2, -50, expression(paste(theta, "' = ", frac(1, 2), " * ", italic(paste(omega^2)), " * t^2 + ", italic(theta))), col = "blue")
# text(7.5, -100, expression(paste(theta, "' = ", frac(1, 2), " * ", italic(paste(omega^2)), " * t^2 + ", italic(omega), " * t + ", -theta)), col = "black")
legend("topright", legend = c("Original Data", "Fitted Curve (t <= 2.49)", "Fitted Curve (2.5 < t <= 4.0)"), 
       col = c("#e0147c", "blue", "black"), lty = c(1, 2, 1))
