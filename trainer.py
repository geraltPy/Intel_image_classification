import tensorflow as tf
import time
import os
import shutil


class Trainer(object):
    def __init__(self, model, train_ds, val_ds, batch_size, epochs):
        self.model = model
        self.train_ds = train_ds
        self.val_ds = val_ds
        self.batch_size = batch_size
        self.epochs = epochs

    def train(self, callbacks=None):
        self.model.compile(
            optimizer='adam',
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=['accuracy']
        )

        history = self.model.fit(
            self.train_ds,
            validation_data=self.val_ds,
            epochs=self.epochs,
            batch_size=self.batch_size,
            callbacks=callbacks
        )
        return history

    @staticmethod
    def tensorboard_logs(log_dir):
        if os.path.exists(log_dir):  # Empties directory if already exists
            shutil.rmtree(log_dir, ignore_errors=True)

        calls = tf.keras.callbacks.TensorBoard(
            log_dir=log_dir,
            histogram_freq=1
        )
        return calls

    @staticmethod
    def save_checkpoint(path):
        if os.path.exists(path):  # Empties directory if already exists
            shutil.rmtree(path, ignore_errors=True)

        save_model = tf.keras.callbacks.ModelCheckpoint(
            filepath=path,
            verbose=1,
            save_best_only=True,
            save_freq='epoch'

        )
        return save_model
