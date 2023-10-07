import luggage from './img/luggage-icon.png'
import edit_button from './img/frame.svg'
import alert_icon from './img/alert-icon.png'
import menu_1 from './img/menu-1.svg'
import arrow from './img/frame-1.svg'
import maximize_2_1 from './img/maximize.svg'
import pin from './img/icons8-pin-100-1.png'
import './style.css'
import './globals.css'
import {useEffect, useState} from "react";

function App() {
  const [flightData, setFlightData] = useState({});
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch flight data from the backend API
    fetch('http://18.153.49.188:5000/get_arrival_time?flight_number=DL1736&departure_date=01/01/2022')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => {
        setFlightData(data);
      })
      .catch((error) => {
        setError(error);
      });
  }, []);

  return (
      <div className="optiflow-hub-static">
        <div className="div">
          <div className="overlap">
            <div className="maximise-button"><img className="maximize" src={maximize_2_1} alt='maximize'/></div>
            <img className="pin" src={pin} alt='pin'/>
            <div className="you">
              <div className="overlap-group">
                <div className="text-wrapper">You</div>
              </div>
            </div>
          </div>
          <p className="here-s-your-optiflow">
            Here’s your OptiFlow for {flightData.flight_number}.<br/>Your flight on {flightData.departure_date} is on time.
          </p>
          <p className="today-is-friday">Today is {new Date().toLocaleDateString()}.<br/>It is currently {new Date().getHours()}:{new Date().getMinutes()}.</p>
          <p className="p">Go to airline check-in portal (British Airways).</p>
          <div className="overlap-2">
            <div className="RAT-expanded">
              <div className="overlap-group-2">
                <div className="text-wrapper-2">Go to {flightData.departure_airport} at:</div>
                <div className="text-wrapper-3">{flightData.arrival_time}</div>
              </div>
            </div>
          </div>
          <div className="recommended-arrival">
            <div className="overlap-3">
              <p className="text-wrapper-4">To get from the entrance to your gate:</p>
              <div className="text-wrapper-5">{flightData.walking_time} minutes</div>
              <p className="text-wrapper-6">To check in your luggage:</p>
              <div className="text-wrapper-7">{flightData.checkin_time} minutes</div>
              <div className="text-wrapper-8">To go through security:</div>
              <div className="text-wrapper-9">{flightData.security_time} minutes</div>
            </div>
          </div>
          <div className="estimated-details">
            <div className="overlap-4">
              <div className="rectangle"></div>
              <div className="rectangle-2"></div>
              <div className="text-wrapper-10">Scheduled flight time</div>
              <div className="text-wrapper-11">{flightData.scheduled_departure_time}</div>
              <div className="text-wrapper-12">Actual flight time</div>
              <div className="text-wrapper-13">{flightData.actual_departure_time}</div>
              <div className="text-wrapper-14">Usual gate</div>
              <div className="text-wrapper-15">{flightData.gate}</div>
              <div className="text-wrapper-16">Actual gate</div>
              <div className="text-wrapper-17">{flightData.gate}</div>
            </div>
          </div>
          <div className="ticket">
            <div className="overlap-5">
              <div className="overlap-6">
                <div className="text-wrapper-18">Flight</div>
                <div className="text-wrapper-19">{flightData.flight_number}</div>
              </div>
              <div className="overlap-group-3">
                <div className="text-wrapper-20">From</div>
                <div className="text-wrapper-21">{flightData.departure_airport}</div>
              </div>
              <div className="overlap-7">
                <div className="text-wrapper-24">To</div>
                <div className="text-wrapper-25">{flightData.arrival_airport}</div>
              </div>
            </div>
          </div>
          <div className="opti-flow">
            <div className="div-wrapper">
              <div className="text-wrapper-26">OptiFlow</div>
            </div>
          </div>
          <img className="menu" src={menu_1} alt='menu'/>
          <div className="overlap-8">
            <div className="accessibility-icon"></div>
            <div className="text-wrapper-27">I have accessibility needs.</div>
            <div className="text-wrapper-28">I have extra luggage.</div>
            <div className="edit-button"><img className="frame" src={edit_button} alt='edit'/></div>
            <img className="luggage-icon" src={luggage} alt='luggage'/>
          </div>
          <div className="overlap-9">
            <div className="text-wrapper-29">Alerts</div>
            <img className="alert-icon" src={alert_icon} alt='alert'/>
          </div>
          <div className="overlap-10">
            <div className="text-wrapper-30">Share</div>
            <img className="img" src={arrow} alt='arrow'/>
          </div>
          <p className="text-wrapper-31">OptiFlow @ BCG Platinion Hackathon, 2023.</p>
          <div className="overlap-wrapper">
            <div className="overlap-11">
              <div className="text-wrapper-32">OptiFlow</div>
            </div>
          </div>
        </div>
      </div>
  );
}

export default App;
