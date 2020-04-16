from src.models import make_svm_model
from src.models import make_dt_model
from src.models import make_nn_model
from src.models import make_nb_model
import paths
import os.path
import sklearn.metrics
import matplotlib.pyplot as plt
import time


def auto_label(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2., 1.00 * height, '%s' % format(height, '.2f'),
                 ha='center', va='bottom')


def compare(processed_file_path, split):
    time_initial = time.time_ns()
    result_svm, y_test_svm = make_svm_model.make_svm_model(processed_file_path, split)
    time_after_svm = time.time_ns()
    result_dt, y_test_dt = make_dt_model.make_dt_model(processed_file_path, split)
    time_after_dt = time.time_ns()
    result_nn, y_test_nn = make_nn_model.make_nn_model(processed_file_path, split)
    time_after_nn = time.time_ns()
    result_nb, y_test_nb = make_nb_model.make_nb_model(processed_file_path, split)
    time_after_nb = time.time_ns()

    # time in ms
    time_svm = time_after_svm - time_initial
    time_dt = time_after_dt - time_after_svm
    time_nn = time_after_nn - time_after_dt
    time_nb = time_after_nb - time_after_nn

    # for plotting time taken by each
    time_classifiers = {'svm': time_svm,
                        'dt': time_dt,
                        'nn': time_nn,
                        'nb': time_nb}
    print(time_classifiers)

    rects = plt.bar(range(len(time_classifiers)), time_classifiers.values(), align='center', width=0.5)
    auto_label(rects)
    plt.xticks(range(len(time_classifiers)), list(time_classifiers.keys()))
    plt.xlabel('Classifier')
    plt.ylabel('Time taken to train')
    axes = plt.gca()

    # for plotting accuracy
    plt.figure()
    accuracy_scores = {'svm': sklearn.metrics.accuracy_score(y_test_svm, result_svm),
                       'dt': sklearn.metrics.accuracy_score(y_test_dt, result_dt),
                       'nn': sklearn.metrics.accuracy_score(y_test_nn, result_nn),
                       'nb': sklearn.metrics.accuracy_score(y_test_nb, result_nb)}

    rects = plt.bar(range(len(accuracy_scores)), accuracy_scores.values(), align='center', width=0.5)
    auto_label(rects)

    plt.xticks(range(len(accuracy_scores)), list(accuracy_scores.keys()))
    plt.xlabel('Classifier')
    plt.ylabel('Accuracy Score')
    axes = plt.gca()
    axes.set_ylim([0, 1.05])

    # for plotting f1 scores
    plt.figure()
    f1_scores = {'svm': sklearn.metrics.f1_score(y_test_svm, result_svm, average='weighted'),
                 'dt': sklearn.metrics.f1_score(y_test_dt, result_dt, average='weighted'),
                 'nn': sklearn.metrics.f1_score(y_test_nn, result_nn, average='weighted'),
                 'nb': sklearn.metrics.f1_score(y_test_nb, result_nb, average='weighted')}
    rects = plt.bar(range(len(f1_scores)), f1_scores.values(), align='center', width=0.5)
    auto_label(rects)

    plt.xticks(range(len(f1_scores)), list(f1_scores.keys()))
    plt.xlabel('Classifier')
    plt.ylabel('f1 Score')
    axes = plt.gca()
    axes.set_ylim([0, 1.05])

    # for plotting hamming loss
    plt.figure()
    hamming_losses = {'svm': sklearn.metrics.hamming_loss(y_test_svm, result_svm),
                 'dt': sklearn.metrics.hamming_loss(y_test_dt, result_dt),
                 'nn': sklearn.metrics.hamming_loss(y_test_nn, result_nn),
                 'nb': sklearn.metrics.hamming_loss(y_test_nb, result_nb)}
    rects = plt.bar(range(len(hamming_losses)), hamming_losses.values(), align='center', width=0.5)
    auto_label(rects)

    plt.xticks(range(len(hamming_losses)), list(hamming_losses.keys()))
    plt.xlabel('Classifier')
    plt.ylabel('Hamming loss')
    axes = plt.gca()
    axes.set_ylim([0, 1.05])

    # plotting matthews correlation coefficient
    plt.figure()
    matthews_corrcoefs = {'svm': sklearn.metrics.matthews_corrcoef(y_test_svm, result_svm),
                      'dt': sklearn.metrics.matthews_corrcoef(y_test_dt, result_dt),
                      'nn': sklearn.metrics.matthews_corrcoef(y_test_nn, result_nn),
                      'nb': sklearn.metrics.matthews_corrcoef(y_test_nb, result_nb)}
    rects = plt.bar(range(len(matthews_corrcoefs)), matthews_corrcoefs.values(), align='center', width=0.5)
    auto_label(rects)

    plt.xticks(range(len(matthews_corrcoefs)), list(matthews_corrcoefs.keys()))
    plt.xlabel('Classifier')
    plt.ylabel('Matthews correlation coefficient')
    axes = plt.gca()
    axes.set_ylim([0, 1.05])
    plt.show()


if __name__ == "__main__":
    processed_file_path = os.path.join(paths.PROCESSED_DATA_DIR, "qws2_processed.csv")
    compare(processed_file_path, split=0.4)
