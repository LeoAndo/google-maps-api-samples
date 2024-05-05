package com.mapsapiv3.test;

import java.util.List;

import android.app.Activity;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;

public class GmapsApiTestActivity extends Activity implements SensorEventListener {
	private SensorManager sensorManager;
	private WebView webView;
	private static String MAP_PAGE_URL
		= "http://googlemaps.googlermania.com/book_impress/4-4.html";
	
	private Sensor originSensor;
	private int pitch, yaw;
	private Boolean isSensorRegistered = false;
	
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.main);
		
		//センサーマネージャーを取得する
		this.sensorManager = (SensorManager) getSystemService(SENSOR_SERVICE);
		
		//WebViewの初期化
		webView = (WebView)findViewById(R.id.webview);
		WebSettings webSettings = this.webView.getSettings();
		webSettings.setJavaScriptEnabled(true);
		webSettings.setCacheMode(WebSettings.LOAD_NO_CACHE);
		this.webView.setWebChromeClient(new WebChromeClient());
		this.webView.addJavascriptInterface(this, "androidClient");
		this.webView.loadUrl(MAP_PAGE_URL);
	}
	@Override
	public void onResume() {
		super.onResume();
		//センサーの取得
		List<Sensor> sensors = this.sensorManager.getSensorList(Sensor.TYPE_ORIENTATION);
		if (sensors.size() > 0) {
			this.originSensor = sensors.get(0);
			this.sensorManager.registerListener(this, this.originSensor, SensorManager.SENSOR_DELAY_UI);
			this.isSensorRegistered = true;
		}
	}
	@Override
	public void onPause() {
		if (this.isSensorRegistered) {
			this.sensorManager.unregisterListener(this);
			this.isSensorRegistered = false;
		}
		super.onPause();
	}
	public void onAccuracyChanged(Sensor sensor, int accuracy) {}
	
	public void onSensorChanged(SensorEvent event) {
		if (event.accuracy == SensorManager.SENSOR_STATUS_UNRELIABLE) {
			return;
		}
		if (event.sensor.getType() == Sensor.TYPE_ORIENTATION) {
			this.yaw = (int)event.values[0];
			this.pitch = (int)event.values[1];
		}
	}

	public String getPov() {
		if (this.isSensorRegistered == false) {
			return "";
		}
		return this.yaw +"," + this.pitch;
	}
}