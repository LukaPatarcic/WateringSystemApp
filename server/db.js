const db = require('quick.db');
const TOKENS = 'tokens'
const WATER_LEVEL = 'waterLevel'

function saveToken(token) {
    const tokens = db.get(TOKENS);
    if(!tokens?.includes(token))
        db.push(TOKENS, token);
}

function getTokens() {
    return db.get(TOKENS);
}

function saveWaterLevel(waterLevel) {
    db.set(WATER_LEVEL, waterLevel);
}

function getWaterLevel() {
    return db.get(WATER_LEVEL)
}

module.exports = { saveToken, getTokens, saveWaterLevel, getWaterLevel }