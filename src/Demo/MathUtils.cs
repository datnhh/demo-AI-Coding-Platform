namespace Demo;

/// <summary>
/// Vài phép toán đơn giản trên số.
/// </summary>
public static class MathUtils
{
    /// <summary>Trả về số nhỏ hơn trong 2 số tự nhiên. Kết quả không bao giờ nhỏ hơn 0.</summary>
    public static int Min(int a, int b) => Math.Max(0, Math.Min(a, b));
}
