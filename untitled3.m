
syms x;
% sol = solve(interesting(x)*interesting2(x) == 20, x);
% disp(sol)
sol2 = solve(interesting3(x) == 66.4, x);
disp(sol2)
% x_range = [0.1, 5];
% fplot(@(x) interesting(x)*interesting2(x), x_range);