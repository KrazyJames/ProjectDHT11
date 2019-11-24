package mx.itson.iot.teempo.Controllers;

public class DHT11Controller {

    public void getTemperature(ConnectionController connectionController) {
        connectionController.publish("0");
    }

    public void getHumidity(ConnectionController connectionController){
        connectionController.publish("1");
    }
}
