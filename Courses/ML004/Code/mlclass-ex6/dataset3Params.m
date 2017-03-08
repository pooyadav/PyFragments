function [C, sigma] = dataset3Params(X, y, Xval, yval)
%EX6PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = EX6PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
% C = 1;
% sigma = 0.3;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%
% results = zeros(64, 3);
% elect = [0.01 0.03 0.1 0.3 1 3 10 30];
% i = 1;
% for C = elect
%     for sigma = elect
%         model= svmTrain(X, y, C, @(x1, x2) gaussianKernel(x1, x2, sigma));
%         predictions = svmPredict(model, Xval);
%         pe = mean(double(predictions ~= yval));
%         results(i,:) = [pe C sigma];
%         i = i + 1;
%     end
% end

% disp(results);
% [~, I] = min(results(:,1));
% display(results(I,:)); %0.0300    1.0000    0.1000

C = 1;
sigma = 0.1;


% =========================================================================

end
