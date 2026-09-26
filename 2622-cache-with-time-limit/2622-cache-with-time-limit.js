class TimeLimitedCache {
    constructor() {
        this.cache = new Map();
    }

    set(key, value, duration) {
        const existing = this.cache.get(key);

        // If key already exists, cancel its old timer
        if (existing) {
            clearTimeout(existing.timer);
        }

        // Create a new timer
        const timer = setTimeout(() => {
            this.cache.delete(key);
        }, duration);

        // Store value and timer
        this.cache.set(key, {
            value: value,
            timer: timer
        });

        // true if key existed, false otherwise
        return existing !== undefined;
    }

    get(key) {
        if (!this.cache.has(key)) {
            return -1;
        }

        return this.cache.get(key).value;
    }

    count() {
        return this.cache.size;
    }
}