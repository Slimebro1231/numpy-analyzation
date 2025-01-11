% FILEPATH: /Users/max/Desktop/numpy analyzation/math.m
% Import the data
data = importdata('data1.txt');
t = data.data(:, 1);
theta = data.data(:, 2);

% Convert degrees to radians
theta = deg2rad(theta);

% Splitting the data
t_1 = t(t <= 2.49);
theta_1 = theta(t <= 2.49);

t_2 = t(t > 2.5 & t <= 4.0);  % New range for the second curve
theta_2 = theta(t > 2.5 & t <= 4.0);

% Define the functions
func_1 = @(t, angular_accel, initial_angle) 0.5 * angular_accel * t.^2 + initial_angle;
func_2 = @(t, angular_accel, initial_velocity, initial_angle) 0.5 * angular_accel * t.^2 + initial_velocity * t + initial_angle;

% Curve fit with bounds
angular_acceleration = -16.7813;
angular_deceleration_min = -2.8273;
angular_deceleration = -3.5743;
initial_angle = -48.723;
popt_1 = lsqcurvefit(func_1, [angular_acceleration, initial_angle], t_1, theta_1);
popt_2 = lsqcurvefit(func_2, [angular_deceleration, 0, initial_angle], t_2, theta_2, [angular_deceleration, -Inf, -initial_angle], [angular_deceleration_min, Inf, -initial_angle]);

% Generate fit
fit_curve_1 = func_1(t_1, popt_1(1), popt_1(2));
fit_curve_2 = func_2(t_2, popt_2(1), popt_2(2), popt_2(3));

% Plotting the original data
figure;
plot(t, theta, 'o', 'MarkerSize', 4, 'LineStyle', '-', 'Color', '#e0147c', 'DisplayName', 'Original Data');
hold on;

% Plotting the fitted curves
plot(t_1, fit_curve_1, 'LineStyle', '--', 'Color', 'blue', 'DisplayName', 'Fitted Curve (t <= 2.49)');
plot(t_2, fit_curve_2, 'LineStyle', '-', 'Color', 'black', 'DisplayName', 'Fitted Curve (2.5 < t <= 4.0)');

% Calculate correlation coefficients
corrcoef_1 = corr(theta_1, fit_curve_1);
corrcoef_2 = corr(theta_2, fit_curve_2);

% Display equations and correlation coefficients
eq_1 = sprintf('θ'' = 0.5 * %.2f * t^2 + %.2f\nCorrelation: %.8f', popt_1(1), popt_1(2), corrcoef_1);
eq_2 = sprintf('θ'' = 0.5 * %.4f * t^2 + %.2f * t + %.2f\nCorrelation: %.8f', abs(popt_2(1)), popt_2(2), popt_2(3), corrcoef_2);

text(4.2, -50, eq_1, 'FontSize', 10, 'Color', 'blue');
text(7.5, -100, eq_2, 'FontSize', 10, 'Color', 'black');

% Plotting the arrows
midpoint_1 = [(t_1(1) + t_1(end)) / 2 + 0.5, (fit_curve_1(1) + fit_curve_1(end)) / 2 + 0.5];
midpoint_2 = [(t_2(1) + t_2(end)) / 2, (fit_curve_2(1) + fit_curve_2(end)) / 2];
arrow_1 = FancyArrowPatch([midpoint_1(1), 4.1], [midpoint_1(2), -35], 'LineStyle', '--', 'Color', 'blue');
arrow_2 = FancyArrowPatch([midpoint_2(1), 7.3], [midpoint_2(2), -85], 'LineStyle', '--', 'Color', 'black');
ax = gca;
ax.Children = [ax.Children, arrow_1, arrow_2];

% Plot settings
grid on;
title('θt graph for disc motion');
xlabel('t (seconds)');
ylabel('θ (radians)');
legend('Location', 'best');
ax.XAxisLocation = 'origin';
ax.YAxisLocation = 'origin';
ax.XLim = [min(t), max(t)];
ax.YLim = [min(theta), max(theta)];
ax.XTick = [0, 2.5, 4];
ax.YTick = linspace(min(theta), max(theta), 5);
