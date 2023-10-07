# %%
# set key
BingMapsKey = AuWIe6XEy8zl7Gt4DM6kMVqIUKyzkGDJtYN698kZ-yx9jD3EEqqTJjBZV6KJEmFh

# %%
# find route
# blank URL: http://dev.virtualearth.net/REST/v1/Routes?wayPoint.1={wayPoint1}&viaWaypoint.2={viaWaypoint2}&waypoint.3={waypoint3}&wayPoint.n={waypointN}&heading={heading}&optimize={optimize}&avoid={avoid}&distanceBeforeFirstTurn={distanceBeforeFirstTurn}&routeAttributes={routeAttributes}&timeType={timeType}&dateTime={dateTime}&maxSolutions={maxSolutions}&tolerances={tolerances}&distanceUnit={distanceUnit}&key={BingMapsKey}

wayPoint1 = Seattle,WA
waypoint2 = Seattle,WA

url = f"http://dev.virtualearth.net/REST/v1/Routes?wayPoint.1={wayPoint1}&viaWaypoint.2={viaWaypoint2}&waypoint.3={waypoint3}&heading={heading}&optimize={optimize}&avoid={avoid}&distanceBeforeFirstTurn={distanceBeforeFirstTurn}&routeAttributes={routeAttributes}&timeType={timeType}&dateTime={dateTime}&maxSolutions={maxSolutions}&tolerances={tolerances}&distanceUnit={distanceUnit}&key={BingMapsKey}"