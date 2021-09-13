package com.javapp;

import com.javapp.controller.Controller;
import com.javapp.model.Modelo;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class App extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        System.out.println(App.class.getResource("ventanaPrincipal.fxml"));
        Controller controller = new Controller();
        FXMLLoader fxmlLoader = new FXMLLoader(App.class.getResource("ventanaPrincipal.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 720 , 480);
        stage.setScene(scene);
        stage.show();

    }

    public static void main(String[] args) {
        launch();
    }
}