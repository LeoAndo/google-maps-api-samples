function SearchBox() {
	//テンプレート
	this.tmpl = '<div id="searchbox" class="searchbox">\
			<input name="q" id="q" type="text" value=""/>\
			<button action="search">地名検索</button>\
			<button action="clear">クリア</button>\
		</div>';
	
	this.searchService_ = new google.maps.Geocoder();
};

//OverlayViewを継承
SearchBox.prototype = new google.maps.OverlayView();

SearchBox.prototype.onAdd = function() {
	this.map_ = this.getMap();
	
	//div.innerHTMLに一度取り込むことで、evalを使わないでDOM化する
	var dummyDiv = document.createElement("div");
	dummyDiv.innerHTML = this.tmpl;
	this.container_ = dummyDiv.firstChild;
	
	//地図に追加する
	this.map_.controls[google.maps.ControlPosition.BOTTOM_LEFT].push(this.container_);
	
	//テキストエリア
	this.queryBox_ = this.container_.getElementsByTagName("input")[0];
	
	//検索ボタンが押された時の処理
	var buttons = this.container_.getElementsByTagName("button");
	var that = this;
	for (var i = 0; i < buttons.length; i++) {
		google.maps.event.addDomListener(buttons[i], "click", function(evt){
			that.btnClicked_.call(that, evt);
		});
	}
};
SearchBox.prototype.onRemove = function() {
	//地図から削除する
};
SearchBox.prototype.draw = function() {
	//描画処理
};
SearchBox.prototype.btnClicked_ = function(evt) {
	//ボタンがクリックされた
	var action = evt.target.getAttribute('action');
	var queryWord = this.queryBox_.value;
	switch(action) {
		case "search":
			//検索する
			this.execSearch_(queryWord);
			break;
		case "clear":
			//クリアする
			this.queryBox_.value = "";
			break;
	}
};
SearchBox.prototype.execSearch_ = function(queryWord) {
	//検索の実行
	var that = this;
	this.searchService_.geocode({
		"address" : queryWord,
		"bounds" : this.map_.getBounds(),
		"region" : "jp"
	}, function(result, status) {
		that.geocoderResult_.call(that, result, status);
	});
};
SearchBox.prototype.geocoderResult_ = function(results, status) {
	if(status == google.maps.GeocoderStatus.OK) {
		var result = results[0];
		var bounds = result.geometry.bounds;
		var viewport = result.geometry.viewport;
		if(bounds !== undefined) {
			this.map_.fitBounds(bounds);
		} else if(viewport !== undefined) {
			this.map_.fitBounds(viewport);
		} else {
			this.map_.panTo(result.geometry.location);
		}
	} else {
		alert('見つかりませんでした');
	}
};