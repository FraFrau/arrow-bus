package com.javapp.controller;

import com.javapp.model.Modelo;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.Pane;


public class Controller {
    @FXML
    private Label lblResultado;

    @FXML
    private TextField txtPrimerNumero;

    @FXML
    private TextField txtSegundoNumero;

    @FXML
    private Label lblTitulo;

    private Modelo calculadora;

    @FXML
    public void initialize(){
        String versionJava = System.getProperty("java.version");
        String fxVersion   = System.getProperty("javafx.version");
        final byte major = 1;
        final byte minor = 0;
        lblTitulo.setText("Calculadora V."+major+"."+minor+" - Hecha en Java"+versionJava+"@fx"+fxVersion);
        calculadora = new Modelo();
    }

    @FXML
    protected void onBtnSumar() {
        int numeroUno = Integer.parseInt(txtPrimerNumero.getText());
        int numeroDos = Integer.parseInt(txtSegundoNumero.getText());

        lblResultado.setText("El resultado es "+String.valueOf(calculadora.sumar(numeroUno,numeroDos)));
    };



}
